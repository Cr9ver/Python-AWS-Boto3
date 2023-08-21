import boto3

bucket_name = "bucket-name"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(bucket_name, "file-to-download")

s3_object.download_file('downloaded file')