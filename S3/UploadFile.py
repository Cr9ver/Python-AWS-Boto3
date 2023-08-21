import boto3

bucket_name = "bucket-name"

client = boto3.client('s3')


def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    
    client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"{file_name} has been uploaded to {bucket_name}")


upload_files("CreateBucket.py", bucket_name)



