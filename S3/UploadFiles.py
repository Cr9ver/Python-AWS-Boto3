import boto3

client = boto3.client('s3')


with open('test.jpg', 'rb') as file:
    data = file.read()

response = client.put_object(
    Bucket="bucket-name",
    ACL="private",
    Body=data,
    Key='test.jpg'
)

print(response)