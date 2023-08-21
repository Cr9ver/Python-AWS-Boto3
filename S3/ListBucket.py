import boto3

client = boto3.client('s3')

response = client.list_buckets()

print(f'Listing all buckets:')

for number,bucket in enumerate(response['Buckets']):
    print(f"{number + 1}:{bucket['Name']}")


# Method 2

'''
resource = boto3.resource('s3')
iterator = resource.buckets.all()

print("Listing all buckets: ")

for bucket in iterator:
    print(bucket.name)

'''