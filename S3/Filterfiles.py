import boto3

bucket_name= "cr9ver-test-aws"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(bucket_name)

print("Listing filtered files")

for object in s3_bucket.objects.filter(Prefix="myfile"):
    print(object.key)

