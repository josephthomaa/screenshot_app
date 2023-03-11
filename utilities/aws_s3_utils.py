import os 
import boto3
import base64
from io import StringIO


class S3FileUpload():
    def __init__(self):
        self.access_key = base64.b64decode("Key").decode("utf-8")
        self.secret_key = base64.b64decode("Secret").decode("utf-8")
        self.s3_resource = boto3.resource('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        self.s3_bucket = 'bucket_name'
        self.s3_screenshot_upload_path = 'screenshots/'
    
    def s3_upload_file(self, local_file_name, s3_file_name):
        try:
            self.s3_resource.meta.client.upload_file(Filename=local_file_name, Bucket=self.s3_bucket, Key=self.s3_screenshot_upload_path+s3_file_name)
        except Exception as e:
            print(f"Error in uploading {str(e)}")
    
