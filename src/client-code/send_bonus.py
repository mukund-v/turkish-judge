import boto3
import sys
import csv



def main(inputfile, bonuses_given):
    ''' Code to send a bonus to workers who provide extra work on the HIT. For our HIT that is providng more than two responses for
    a given conversation. The inputfile read in is the file creaetd by get_results.py'''

    MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
    mturk = boto3.client('mturk',
    aws_access_key_id = "AKIAQNR5F4WWO25SACX6",
    aws_secret_access_key = "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",
    region_name='us-east-1'
    # endpoint_url = MTURK_SANDBOX  # to access MTurk marketplace leave out endpoint_url completely
    )

    worker_assignment = []
    with open(inputfile,'r') as input:
        reader = csv.reader(input)
        header = next(reader)
        for row in reader:          # for the task we are analyzing here, responses are in row[8]-row[57]
            assignmentID = row[0]
            workerID = row[1]
            responses = 0
            for i in range(9,59):
                if row[i].strip()!="NA" and row[i].strip()!=".":
                    responses+=1
            extra_work = responses - 20
            if extra_work > 0:
                if extra_work < 10:
                    bonus = "00.0{}".format(extra_work)
                else:
                    bonus = "00.{}".format(extra_work)
                reason = "Provided {} extra responses".format(extra_work)
                print("Giving worker {} a bonus of {} dollars for reason: {}".format(workerID,bonus,reason))
                mturk.send_bonus(WorkerId=workerID,AssignmentId=assignmentID,BonusAmount=bonus,Reason=reason)
                print("Bonus given")
                worker_assignment.append((workerID,assignmentID,bonus,reason))
            else:
                print("Worker {} is not receiving any bonus".format(workerID))
    with open(bonuses_given, 'w') as output:
        wr = csv.writer(output)
        wr.writerows(worker_assignment)




if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
