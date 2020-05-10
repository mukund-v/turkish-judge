import pandas as pd
import json as json

def parse_csv(input):
    df = pd.read_csv(input)
    rejected = df[
        df["AssignmentStatus"]=="Submitted"  # the csv we're using rn has 'Submitted' not 'Approved'
    ]
    only_relevant_columns = rejected[["WorkerId", "AssignmentId", "HITId", "Answer"]]
    rejected_w_id = only_relevant_columns.rename(columns={"AssignmentId":"_id"})
    return json.loads(rejected_w_id.to_json(orient='records'))