import boto3
from pprint import pprint

# pprint is apython module to print data structures in a readable way 

client = boto3.client('s3')

# response = client.get_bucket_website(
#     Bucket="cr9ver-query"
# )

# pprint(response)

response = client.get_bucket_location(
    Bucket="cr9ver-query"
)

pprint(response)