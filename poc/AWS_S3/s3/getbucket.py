from enum import Enum

from botocore.client import BaseClient
from fastapi import Depends

from s3_connect import s3_con


def get_list_of_buckets(s3: BaseClient = Depends(s3_con)):
    response = s3.list_buckets()
    buckets = {}

    for buckets in response['Buckets']:
        buckets[response['Name']] = response['Name']pi

    BucketName = Enum('BucketName', buckets)

    return BucketName