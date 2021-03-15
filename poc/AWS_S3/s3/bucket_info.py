from fastapi import APIRouter, Depends
from s3_connect import s3_con
from botocore.client import BaseClient


router = APIRouter()


@router.get("/")
def get_buckets(s3: BaseClient = Depends(s3_con)):
    response = s3.list_buckets()

    return response['Buckets']