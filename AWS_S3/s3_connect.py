import boto3
from botocore.client import BaseClient

session = boto3.Session()

credentials = session.get_credentials()
access_key = credentials.access_key
secret_key = credentials.secret_key
# uses credentials from environment
def s3_auth() -> BaseClient:
    s3 = boto3.client(service_name='s3', aws_access_key_id= access_key,
                      aws_secret_access_key= secret_key
                      )

    return s3

s3=s3_auth()
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')








