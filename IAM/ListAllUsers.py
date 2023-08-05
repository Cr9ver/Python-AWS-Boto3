import boto3

#Method1
# def all_users():
#     iam = boto3.client('iam')

#     paginator = iam.get_paginator('list_users')

#     for response in paginator.paginate():
#         for user in response['Users']:
#             username =  user['UserName']
#             Arn = user['Arn']
#             print(f'Username: {username} Arn: {Arn}')

# all_users()

#Method2
iam = boto3.client('iam')
responselist = iam.list_users()


for username in responselist['Users']:
    user = username['UserName']
    arn = username['Arn']
    print(f'{user}: {arn}')




