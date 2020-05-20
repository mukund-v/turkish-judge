import pandas as pd
import json as json
import csv 
import boto3
import xmltodict
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, Template
from example import example_question, example_answer


with open("config.json", 'r') as input:
    config = json.loads(input.read())

# TODO this method shoud be able to accept arbitrary column names that indicate rejections
def parse_csv(input):
    df = pd.read_csv(input)
    rejected = df[
        df["AssignmentStatus"]=="Approved"  # TODO change to 'Rejected' testing csv has all 'Approved'
    ]
    only_relevant_columns = rejected[["WorkerId", "AssignmentId", "HITId", "Question", "Answer"]]
    rejected_w_id = only_relevant_columns.rename(columns={"AssignmentId":"_id"})
    reject_json = json.loads(rejected_w_id.to_json(orient='records'))
    for hit in reject_json:
        hit["Status"] = "NA"
        hit["sandboxLink"] = create_task(question_xml=hit["Question"], answer_xml=hit["Answer"], HITId=hit["_id"])
    return reject_json

def align_xmls(question_xml, answer_xml):
    question = BeautifulSoup(question_xml, 'lxml')
    answer = BeautifulSoup(answer_xml, 'lxml')
    questions = question.find_all("input")
    answers = answer.find_all("answer")
    for ans in answers:
        if ans.find("freetext").text=="true":
            q_id = ans.find("questionidentifier").text
            q_id_split = q_id.split(".")
            q_number = q_id_split[0]
            q_value = q_id_split[1]
            for q in questions:
                if q["name"]==q_number and q["value"]==q_value:
                    q["checked"] = "checked"
    with open("templates1/task.html", 'w') as output:
        print (question.find("crowd-form"),file=output)

def create_appeal(sandbox_link, explanation):
    mturk = connect_to_MTurk()
    new_hit = mturk.create_hit(
        Title = 'Adjudicate appealed HIT rejections',
        Description = 'Judge whether the rejectection was fair or unfair',
        Keywords = 'fairness, jury, adjudication',
        Reward = '0.01',
        MaxAssignments = 5,
        LifetimeInSeconds = 1209600,
        AssignmentDurationInSeconds = 5400,
        AutoApprovalDelayInSeconds = 3600,
        QualificationRequirements = [],
        HITLayoutId = "3S61CKY9NO0FW7HAPT77VH7YQLZOB2", # this Id is for sandbox, there is a different one for marketplace
        HITLayoutParameters = [
          {
            "Name": "explanation",
            "Value": explanation
          },
          {
            "Name": "sandboxLink",
            "Value": sandbox_link
          }
        ]
    )
    print ("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
    return new_hit['HIT']['HITId']
    


def create_task(question_xml, answer_xml, HITId):
    mturk = connect_to_MTurk()
    align_xmls(question_xml=question_xml, answer_xml=answer_xml)
    fileloader = FileSystemLoader('templates1')      # Accesses the directory 'templates' in the same classpath as this code file. 'templates' contains files for HTML/XML templates
    env = Environment(loader=fileloader)            # Establishes the environment to load a specific file from the templates diretory
    task_template = env.get_template('task.xml')
    output = task_template.render()

    with open('task.xml', 'w') as f:
      print(output,file=f)
    task = open(file='task.xml',mode='r').read()
    new_hit = mturk.create_hit(
        Title = 'Appeal of {} TEST2'.format(HITId),
        Description = 'Review this filled out HIT to determine whether the worker completed it correctly',
        Keywords = 'fairness, jury, adjudication',
        Reward = '0.01',
        MaxAssignments = 5,
        LifetimeInSeconds = 1209600,
        AssignmentDurationInSeconds = 5400,
        AutoApprovalDelayInSeconds =3600,
        QualificationRequirements = [],
        Question = task
    )
    print ("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
    return "https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId']

def get_results(HITID):
  mturk = connect_to_MTurk()
  keys = config["HITkeys"]
  all_results = []
  results = mturk.list_assignments_for_hit(HITId=HITID, AssignmentStatuses=["Submitted"])
  if results['NumResults'] > 0:  
      for assignment in results['Assignments']:   
          xml_doc = xmltodict.parse(assignment['Answer'])
          print("Worker's answer was:")
          print("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
          print("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
          assignment[xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier']] = xml_doc['QuestionFormAnswers']['Answer']['FreeText']
          all_results.append(assignment)
          mturk.approve_assignment(AssignmentId=assignment["AssignmentId"])
  return pd.DataFrame(all_results, columns=keys)


def connect_to_MTurk(sandbox=True):
  '''
  Method to create an instance of an MTurk requester client.
  Arg1: Boolean for whether this client should connect to sandbox (True) or 
  connect to the actual marketplace (False)
  '''
  access_key = config["AWSkey"]
  secret_key = config["AWSsecret"]
  MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
  if sandbox:
    mturk = boto3.client('mturk',
       aws_access_key_id = access_key,
       aws_secret_access_key = secret_key,
       region_name='us-east-1',
       endpoint_url = MTURK_SANDBOX  # to access MTurk marketplace leave out endpoint_url completely
    )
  else:
    mturk = boto3.client('mturk',
       aws_access_key_id = access_key,
       aws_secret_access_key = secret_key,
       region_name='us-east-1'
    )
  return mturk

def writecsvfile(outputfile,rows,keys):
    '''Method to write the dictionary information in rows to a csv file passed as outputfile. keys is the list of keys for the dictionary'''
    with open(outputfile, 'w') as output:
        writer = csv.DictWriter(output,keys,restval="NA")
        writer.writeheader()
        writer.writerows(rows)

def writetxtfile(outputfile, rows):
    with open(outputfile,'w') as f:
        for item in rows:
            f.write("%s\n" % item)

def readfiles(files):
    '''Method to read in files passed in a list, concatenate all of their rows into one list rows and return that data'''
    rows = []
    for inputfile in files:
        with open(inputfile, 'r') as input:
            reader = csv.DictReader(input, next(input).split(","))
            rows.extend([row for row in reader])
    return rows

def writeIDS(inputfile,outputfile):
  rows = []
  with open(inputfile, 'r') as input:
    for i,line in enumerate(input):
      if i % 3 == 1:
        rows.append(line.split(" ")[2])

  writetxtfile(outputfile,rows)

