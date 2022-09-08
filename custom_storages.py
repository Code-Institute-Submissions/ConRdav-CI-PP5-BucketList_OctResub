from django.cong import settings
from storages.backends.s3boto3 import S3Botot3Storage


class StaticStorage(S3Botot3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Botot3Storage):
    location = settings.MEDIAFILES_LOCATION
