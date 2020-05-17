import pandas as pd
import json as json
import csv 
import boto3
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, Template
from example import example_question, example_answer

def parse_csv(input):
    df = pd.read_csv(input)
    rejected = df[
        df["AssignmentStatus"]=="Submitted"  # the csv we're using rn has 'Submitted' not 'Approved'
    ]
    only_relevant_columns = rejected[["WorkerId", "AssignmentId", "HITId", "Answer"]]
    rejected_w_id = only_relevant_columns.rename(columns={"AssignmentId":"_id"})
    reject_json = json.loads(rejected_w_id.to_json(orient='records'))
    for hit in reject_json:
        hit["Status"] = "NA"
    return reject_json


def align_xmls(question_xml, answer_xml):

    question = BeautifulSoup(question_xml, 'lxml')
    answer = BeautifulSoup(answer_xml, 'xml')
    questions = question.find_all("input")
    answers = answer.find_all("Answer")
    for answer in answers:
        if answer.find("FreeText").text=="true":
            q_id = answer.find("QuestionIdentifier").text
            q_id_split = q_id.split(".")
            q_number = q_id_split[0]
            q_value = q_id_split[1]
            for q in questions:
                if q["name"]==q_number and q["value"]==q_value:
                    parent = q.parent.parent.parent
                    question_tag = question.new_tag("p")
                    question_tag.string = "Worker answered: {}".format(q_value)
                    parent.append(question_tag)
                    #question_xml.replace(parent, parent+"<p>Worker answered: {}</p>".format(q_value))
        
    #for question in questions:
    #    print (question.parent.parent.parent)
    #    print ("<<<<------------>>>>")
    again = question.find_all("input")
    with open("task.html", 'w') as output:
        print (question.find("crowd-form"),file=output)

def create_task():
    mturk = connect_to_MTurk()
    fileloader = FileSystemLoader('templates1')      # Accesses the directory 'templates' in the same classpath as this code file. 'templates' contains files for HTML/XML templates
    env = Environment(loader=fileloader)            # Establishes the environment to load a specific file from the templates diretory

    task_template = env.get_template('task.xml')

    output = task_template.render()

    with open('task.xml', 'w') as f:
      print(output,file=f)
    task = open(file='task.xml',mode='r').read()
    new_hit = mturk.create_hit(
        Title = 'turkish judge',
        Description = 'Decide whether the task included in this HIT was fairly or unfairly rejected',
        Keywords = 'fairness, jury, adjudication',
        Reward = '0.35',
        MaxAssignments = 3,
        LifetimeInSeconds = 648000,
        AssignmentDurationInSeconds = 5400,
        AutoApprovalDelayInSeconds = 259200,
        QualificationRequirements = [],
        Question = task
    )

    print("A new HIT has been created. You can preview it here:")
    print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
    print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")



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


if __name__=="__main__":
    with open("config.json", 'r') as input:
        config = json.loads(input.read())
    align_xmls(
        question_xml=example_question(), 
        answer_xml=example_answer())
    create_task()