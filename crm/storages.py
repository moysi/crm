from storages.backends.s3boto3 import S3BotoStorage

class MediaStore(S3BotoStorage):
    location = 'images'
    file_overwrite = False