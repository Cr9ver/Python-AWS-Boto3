import boto3



def detach_policy(username,arn):
    iam = boto3.client("iam")
    response = iam.detach_user_policy(UserName=username,
                                      PolicyArn=arn)
    print(response)


detach_policy(username="username", arn="policyARN")