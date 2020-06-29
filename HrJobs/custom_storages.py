import boto3
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
s3 = boto3.client('s3',
                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                  endpoint_url=settings.AWS_S3_ENDPOINT_URL)

class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"

class MediaRootS3RootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
