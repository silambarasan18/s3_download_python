import os
import boto3

import botocore

# Set up AWS credentials and region
# aws_access_key_id = 'your_access_key_id'
# aws_secret_access_key = 'your_secret_access_key'
# region = 'us-east-1'

# Create an S3 client
# when access key 
# s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
client = boto3.client('s3')

#bucket name
bucket = 'billing-report-trial'
# Specify the S3 prefix and file name to download
s3_prefix = 'billing-report-trial/trial/20230801-20230901/'
file_name = 'trial-00001.csv.zip'

# Specify the local path where the file will be downloaded
cur_path = os.getcwd()

local_file_path = os.path.join(cur_path,'downloads', file_name)
print(local_file_path)

try:
    # Download the specified file
    client.download_file(
        Bucket = bucket,
        Key = s3_prefix + file_name, 
        Filename = local_file_path
        
    )
    
    print(f"File '{file_name}' downloaded successfully to '{local_file_path}'.")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print(f"File '{file_name}' not found in the specified S3 prefix.")
    else:
        print(f"Error downloading file: {e}")
