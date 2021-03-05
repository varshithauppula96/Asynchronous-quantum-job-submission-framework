from botocore.client import BaseClient
import boto3
from env_settings import settings
session = boto3.Session()


access_key = settings.AWS_ACCESS_KEY_ID
secret_key = settings.AWS_SECRET_ACCESS_KEY
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