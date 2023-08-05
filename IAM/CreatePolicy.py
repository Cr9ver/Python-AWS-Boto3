import boto3
import json

filepath = r"IAM\Policies\EC2FullacessPolicy.json"

def create_policy():
    iam = boto3.client('iam')
    with open(filepath, "r") as file:
        policy_document = json.load(file)

    response = iam.create_policy(
        PolicyName = "pyEC2fullAcess",
        PolicyDocument= json.dumps(policy_document)
    )
    print(response)

create_policy()




