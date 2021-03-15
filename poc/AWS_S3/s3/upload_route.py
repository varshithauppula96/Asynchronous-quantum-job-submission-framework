from botocore.client import BaseClient
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

from s3_connect import s3_con
from upload._pending import upload_file_to_bucket

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets",
             description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
             response_description="Successfully uploaded file to S3 bucket")
def upload_file(folder: str, s3: BaseClient = Depends(s3_con), file_obj: UploadFile = File(...)):
    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
                                       bucket='quantumpending',
                                       folder=folder,
                                       object_name=file_obj.filename
                                       )

    if upload_obj:
        return JSONResponse(content="Object has been uploaded to bucket successfully",
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")