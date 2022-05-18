import boto3
#from botocore import UNSIGNED
#from botocore.client import Config

#s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
#s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', region_name='us-east-1')
s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key='')


BUCKET_NAME = "work-sample-mk"
OBJECT_NAME = "2021/04/events.csv"
FILE_NAME = "events.csv"

#s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
s3.meta.client.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
s3.meta.client.download_file('work-sample-mk', '/2021/04/events.csv', 'events.csv')


# import botocore

# BUCKET_NAME = 'work-sample-mk' # replace with your bucket name
# KEY = '/2021/04/events.csv' # replace with your object key

# s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key='', region_name='eu-west-3'), 

# try:
#     s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
# except botocore.exceptions.ClientError as e:
#     if e.response['Error']['Code'] == "404":
#         print("The object does not exist.")
#     else:
#         raise

s3.Bucket('work-sample-mk').download_file('events.csv', '/2021/04/events.csv')