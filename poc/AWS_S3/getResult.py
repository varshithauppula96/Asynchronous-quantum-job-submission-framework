from botocore.client import BaseClient
import boto3
import os
access_key = 'AWS_ACCESS_KEY_ID'
access_value = os.getenv(access_key)
secret_key = 'AWS_SECRET_ACCESS_KEY'
secret_value = os.getenv(secret_key)


# uses credentials from environment
def s3_connect() -> BaseClient:
    s3 = boto3.client(
    's3',
    aws_access_key_id=access_value,
    aws_secret_access_key=secret_value,

)
    return s3

s3=s3_connect()
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
