import boto3

bucket_name = "cr9ver-python-test"

s3_resource = boto3.resource("s3")

s3_bucket = s3_resource.Bucket(bucket_name)

def clean_up():

    #Delete all objects in the bucket 
    for s3_object in s3_bucket.objects.all():
            s3_object.delete()
    
    # Delete bucket versioning if enabled
    for s3_object_ver in s3_bucket.object_versions.all():
          s3_object_ver.delete()
    
    print("S3 bucket cleaned")

clean_up()

s3_bucket.delete()
print("The s3 bucket has been deleted")


