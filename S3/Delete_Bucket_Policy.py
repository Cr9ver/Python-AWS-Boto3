import boto3
from pprint import pprint

bucket="bucket-name"

client = boto3.client('s3')
response = client.delete_bucket_policy(
    Bucket=bucket
)
response=client.list_buckets
pprint(response)