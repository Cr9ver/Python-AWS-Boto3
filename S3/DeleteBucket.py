import boto3


def delete_bucket():
    client = boto3.client('s3')
    bucket_name = "bucket-name"
    response = client.delete_bucket(Bucket=bucket_name)
    print(f"{bucket_name} Bucket has been deleted")


delete_bucket()


'''
or

resource = boto3.resource("s3")

bucket_name = "bucket-name"

s3_bucket = resource.Bucket(bucket_name)
s3_bucket.delete()
print(" This {s3_bucket} bucket has been deleted")
'''