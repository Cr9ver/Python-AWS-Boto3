import boto3

client = boto3.client('s3')
'''
response = client.delete_object(
    Bucket="Bucket", #Bucket name
    Key="copy.pdf" # file to delete
                                )
'''

#delete multiple files

response = client.delete_objects(
    Bucket="cr9ver-query",
    Delete={
        'Objects':[
            {
                'Key': 'copied.pdf' #file to delete also we can pass multiple objects in form of a dictionary
            }
        ]
    }
)
print(response)