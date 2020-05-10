import pandas as pd
import json as json

def parse_csv(input):
    df = pd.read_csv(input)
    rejected = df[df["AssignmentStatus"]=="Approved"][["WorkerId", "AssignmentId", "Answer"]]
    return json.loads(rejected.to_json(orient='records'))