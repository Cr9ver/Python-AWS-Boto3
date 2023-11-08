import boto3

s3 = boto3.resource('s3')

copy_source = {
    'Bucket': "source-bucket", #pass the source bucket name where data should be copied from 
    'Key': 'myfile.txt' # name of file to be copied 
}

# s3.meta.client.copy(copy_source, 'bucket-name', 'file-name' ) #Here pass in the name for the data to be copied to and the new name for the copied file

s3.meta.client.copy(copy_source, Bucket="bucket-name", Key='key')