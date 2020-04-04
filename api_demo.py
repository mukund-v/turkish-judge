import boto3
from .. import aws_credentials as aws

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

aws_key = input('IAM user access key: ')
aws_secret_key = input('IAM user secret key: ')

mturk = boto3.client('mturk',
   aws_access_key_id = aws.ACCESS_KEY,
   aws_secret_access_key = aws.SECRET_ACCESS_KEY,
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

print("I have ${} in my Sandbox account".format(mturk.get_account_balance()['AvailableBalance']))

# question = open(name='questions.xml',mode='r').read()new_hit = mturk.create_hit(
#     Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
#     Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
#     Keywords = 'text, quick, labeling',
#     Reward = '0.15',
#     MaxAssignments = 1,
#     LifetimeInSeconds = 172800,
#     AssignmentDurationInSeconds = 600,
#     AutoApprovalDelayInSeconds = 14400,
#     Question = question,
# )
#
# print("A new HIT has been created. You can preview it here:")
# print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
# print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")

# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=
