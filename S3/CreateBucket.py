import boto3


client = boto3.client('s3')
response = client.create_bucket(
    Bucket= "bucket-name", 
    ACL= "private",
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1' # region in which you want bucket to be created in 
    }

)

print(response)

