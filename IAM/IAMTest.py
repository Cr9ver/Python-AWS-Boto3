import boto3

# iam = boto3.client('iam')
# response = iam.get_user(UserName='itadmin')

# print(response)

s3 = boto3.client('s3')

response = s3.list_buckets()

for buckets in response['Buckets']:
    print(buckets)