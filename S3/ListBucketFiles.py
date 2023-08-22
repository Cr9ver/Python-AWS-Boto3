import boto3

# bucket_name = "bucket-name"

# s3_resource = boto3.resource("s3")

# s3_bucket = s3_resource.Bucket(bucket_name)

# bucket_objects =  s3_bucket.objects.all()

# print("List of items in bucket: ")

# for objects in bucket_objects:
#     print(objects.key)


# Method 2 
def List_Bucket_Objects(bucket_name):
    client = boto3.client("s3")
    response = client.list_objects(Bucket=bucket_name)
    for objects in response['Contents']:
        print(objects['Key'])


#Pass bucket you need to list objects for here 
List_Bucket_Objects("bucket-name")