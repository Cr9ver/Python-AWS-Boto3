import boto3

s3 = boto3.resource("s3")

bucket_name = "bucket-name" #pass bucket name here
object_summary = s3.ObjectSummary(bucket_name=bucket_name, key="myfile") #pass name of the the file in key

print(object_summary)