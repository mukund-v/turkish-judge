import boto3
import sys
import csv
import itertools
from datetime import datetime

def main(credsfile,input,output):
    mturk = connectToMTurk(credsfile, False)
    print (mturk.get_account_balance())
    #listHITS(mturk)
    #workerIDs = readtxtfile(input)
    #description = "Hello, you've been given this qualification because you have the qualification 3EEL9D2EGEGJTS4ZDH30VKL62A608K issued from another account to do the Dialog Breakdown Challenge HITs, and we are switching to using this account for those HITs. A new batch with 300 of those HITs will be posted later today, completing all 300 wll earn a $6 bonus. Please complete them at your earliest convenience. Thank you for your time, enthusiasm, and excellent work completing these HITs!"
    #createAndAssignQualification(mturk, 'Dialog Breakdown Challenge Qualification', 'dialog breakdown challenge', description, 'Active', workerIDs)
    workers = readtxtfile(input)
    #HITs = readcsvfile(input)
    #HITID = readtxtfile(input)
    #getHITs(mturk,HITID,output)
    #createAdditionalAssignments(mturk,HITs)
    #approveAssignments(mturk,HITs)
    #getWorkersWithQual(mturk,'3EEL9D2EGEGJTS4ZDH30VKL62A608K','DBDCworkers.csv')
    #updateQualification(mturk,'3EEL9D2EGEGJTS4ZDH30VKL62A608K', "Hello, you've been given this qualification because you have worked with members of our lab group in the past (on the Empathic Conversations HIT) and did especially good work as well as provided excellent feedback. We would like you to complete the HITs associated with this qualification (Dialog Breakdown Challenge) for us. In total there are 240 HITs, if you complete all of them you will be given a $4 bonus. We estimate completing all 240 will take between 5-6 hours and you will be paid $96 total for your work (excluding the bonus). Thank you for your work in the past and helping on this HIT!")
    #assignQualification(mturk, '3EEL9D2EGEGJTS4ZDH30VKL62A608K', ['A220QDK5FCC1AO'])
    #getQualificationType(mturk, '3EEL9D2EGEGJTS4ZDH30VKL62A608K')
    #rows = readtxtfile(input)
    #rows = ['3GONHBMNHVW81NISLFCO1A4YRYFMZM', '3UV0D2KX1MHMSG2MEZILCO7GT20F4W', '3T8DUCXY0N4X8RQZQEJ1A0XX63M9TU', '3VCK0Q0PO5CHHKX2TMEW8QQCEH6N0V', '3W31J70BASU0367F8PF0BZB9TBYCK8', '3OJX0UFJ0Z5C845OQJ9BFWJZPHT9UL', '3126F2F5F81GBVO9H8Q3X4XB8XHPEF', '31MBOZ6PAOPBNCPXTPR1QZOOIB3CLB', '3KL228NDMVKDKINKABBJ1QWOR3QKGQ', '3MNJFORX8B24OZ6MS41VHGDUTYVF51', '3E6L1VR4XWK07360XNB09MRUPT6F6H', '3RKHNXPHGWUWP0OFUG0055XF0B5UK0', '3KWGG5KP6J0VTU7IT1SGQC3DIGTCMD', '33P2GD6NRNQRKEIVUHT1MQ8P633KHP', '3U18MJKL1UK1BCSI527G3RSDN63CND', '37OPIVELUU1L8199IQGCSC5T1R9HA7', '3GITHABACYJODU0G89IAREJRBFQN2F', '3511RHPADVCFTEEGBMHWFUNAIC6RLW']
    #send_bonus(mturk, rows, output)
    #updateExpiration(mturk,rows)
    #deleteHITs(mturk)
    messageWorker(mturk, workers)


def listHITS(client):
    result = client.list_reviewable_hits(MaxResults=100)
    HITs = result['HITs']
    next_token = result['NextToken']
    print (next_token)
    Ids = []
    for HIT in HITs:
        Ids.append(HIT['HITId'])
    writetxtfile('HITIDS_out.txt', Ids)
    #writecsvfile('all_HITs.csv',HITs,list(HITs[0].keys))

def deleteHITs(client):
    for HIT in ['3GONHBMNHVW81NISLFCO1A4YRYFMZM', '3UV0D2KX1MHMSG2MEZILCO7GT20F4W', '3T8DUCXY0N4X8RQZQEJ1A0XX63M9TU', '3VCK0Q0PO5CHHKX2TMEW8QQCEH6N0V', '3W31J70BASU0367F8PF0BZB9TBYCK8', '3OJX0UFJ0Z5C845OQJ9BFWJZPHT9UL', '3126F2F5F81GBVO9H8Q3X4XB8XHPEF', '31MBOZ6PAOPBNCPXTPR1QZOOIB3CLB', '3KL228NDMVKDKINKABBJ1QWOR3QKGQ', '3MNJFORX8B24OZ6MS41VHGDUTYVF51', '3E6L1VR4XWK07360XNB09MRUPT6F6H', '3RKHNXPHGWUWP0OFUG0055XF0B5UK0', '3KWGG5KP6J0VTU7IT1SGQC3DIGTCMD', '33P2GD6NRNQRKEIVUHT1MQ8P633KHP', '3U18MJKL1UK1BCSI527G3RSDN63CND', '37OPIVELUU1L8199IQGCSC5T1R9HA7', '3GITHABACYJODU0G89IAREJRBFQN2F', '3511RHPADVCFTEEGBMHWFUNAIC6RLW']:
        client.delete_hit(HITId=HIT)

def connectToMTurk(credsfile, sandbox):

    with open(credsfile, 'r') as creds_input:
        for i,line in enumerate(creds_input):
            if i==1:
                comma_split = line.split(",")
                access_key_id = comma_split[0].strip()
                secret_access_key = comma_split[1].strip()


    if sandbox:
        MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
        mturk = boto3.client('mturk',
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key,
            region_name='us-east-1',
            endpoint_url = MTURK_SANDBOX  # to access MTurk marketplace leave out endpoint_url completely
        )
    else:
        mturk = boto3.client('mturk',
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key,
            region_name='us-east-1'
        )
    
    return mturk


def send_bonus(client, rows, output):

    workers = []
    for row in rows:
        if row['WorkerId'] not in workers:
            workers.append(row['WorkerId'])
    worker_dicts = []
    for worker in workers:
        worker_dict = dict.fromkeys(['WorkerId','HITs', 'AssignmentId'])
        worker_dict['WorkerId'] = worker
        worker_dict['HITs'] = 0
        worker_dict['AssignmentId'] = ""
        for row in rows:
            worker_ID = row['WorkerId']
            if worker_ID==worker:
                worker_dict['HITs']+=1
                worker_dict['AssignmentId'] = row['AssignmentId']
        worker_dicts.append(worker_dict)
    bonuses_given = []
    for worker in worker_dicts:
        if worker['HITs']==60 or worker['WorkerId']=='A2VFHTZKUFKG16':
            print('Giving worker {} a bonus of 12 for their work on assignment {}'.format(worker['WorkerId'], worker['AssignmentId']))
            bonus = "12.00"
            reason = "This bonus is being paid out because we realized we were not paying fairly for the time and work required and we hope this is proper compensation for the work you gave us. Thank you for your time and work in completing these HITs. We hope you enjoyed them and will assist us again in the future. "
            client.send_bonus(WorkerId=worker['WorkerId'],AssignmentId=worker['AssignmentId'], BonusAmount=bonus,Reason=reason)
            bonuses_given.append(worker['WorkerId'])


    writetxtfile(output,bonuses_given)

def approveAssignments(client,HITs):

    for assignment in HITs:
        client.approve_assignment(
            AssignmentId = assignment['AssignmentId'],
            RequesterFeedback = "Great job, thank you for your time and work."
        )
        print("Approved assignment {}".format(assignment['AssignmentId']))

def updateExpiration(client, HITs):
    for HIT in HITs:
        client.update_expiration_for_hit(HITId=HIT.strip(), ExpireAt=datetime(2019, 8, 21))


def createAdditionalAssignments(client,HITs):
    for HIT in HITs:
        num_HITs = int(HIT['NumberOfAssignmentsAvailable']) + int(HIT['NumberOfAssignmentsCompleted\n'])
        num_more = 15 - num_HITs
        client.create_additional_assignments_for_hit(HITId=HIT['HITId'],NumberOfAdditionalAssignments=num_more)
        print ("created {} more assignments for HIT {}".format(num_more,HIT['HITId']))

def messageWorker(client, workers):
    print (len(workers))
    # requires that you have approved or rejected work from this worker before
    client.notify_workers(Subject="New breakdown detection HITs",MessageText="Hi, we're messaging to notify you there are more dialog breakdown detection HITs available on the marketplace. The HITs are titled: Identify dialog breakdowns. They pay 65 cents and should not take much time. These HITs are limited to workers with the qualification for having done these HITs previously and we've really appreciated your help and time in the past so we hope you'll do so again.",WorkerIds=workers)
    print("Message sent to workers")

def createAndAssignQualification(client,name,keywords,description,status,workers):

    custom_qualification = client.create_qualification_type(Name=name,Keywords=keywords,Description=description,QualificationTypeStatus=status)
    qualificationtypeid = custom_qualification['QualificationType']['QualificationTypeId']

    assignQualification(client,qualificationtypeid,workers)

    return qualificationtypeid

def assignQualification(client, qualificationtypeid, workers):
    for worker in workers:
        client.associate_qualification_with_worker(QualificationTypeId=qualificationtypeid,WorkerId=worker.strip(),IntegerValue=1)    
        print ("gave worker {} qualification {}".format(worker,qualificationtypeid))

def updateQualification(client, qualificationtypeid, description):
    client.update_qualification_type(QualificationTypeId=qualificationtypeid,Description=description)


def getHITs(client,HITIDs,output):

    HITsinfo = []
    for HITID in HITIDs:
        HIT = client.get_hit(HITId=HITID.strip())
        HITsinfo.append(HIT['HIT'])

    sorteddd = sorted(HITsinfo, key = lambda i: i['CreationTime'])
    writecsvfile(output,sorteddd,list(HITsinfo[0].keys()))

def getQualificationType(client,qualificationtypeid):
    print(client.get_qualification_type(QualificationTypeId=qualificationtypeid))

def getWorkersWithQual(client,qualificationtypeid,output):
    result = client.list_workers_with_qualification_type(QualificationTypeId=qualificationtypeid,MaxResults=100)
    for item in result['Qualifications']:
        print(item['WorkerId'])

def readcsvfile(file):
    rows = []
    with open(file, 'r') as input:
        reader = csv.DictReader(input, next(input).split(","))
        rows.extend([row for row in reader])  
    return rows

def readtxtfile(file):
    lines = []
    with open(file, 'r') as input:
        lines.extend([line.strip() for line in input])
    return lines

def writecsvfile(output,rows,keys):

    with open(output, 'w') as output:
        writer = csv.DictWriter(output,keys,restval="NA")
        writer.writeheader()
        writer.writerows(rows)

def writetxtfile(output,rows):
    with open(output,'w') as f:
        for item in rows:
            f.write("%s\n" % item)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])