import boto3

def list_policies():
    iam = boto3.client('iam')
    response = iam.list_policies(Scope="AWS") #set scope to Local for Customer manages policies, set scope to AWS for AWS managed policies

    for policies in response['Policies']:
        policy_name = policies['PolicyName']
        Arn = policies['Arn']

        print(f'{policy_name}: {Arn}')

list_policies()