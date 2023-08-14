import os
import boto3


#client
client = boto3.client('s3')

#path and other vars
bucket = 'billing-report-trial'

#list
list_files = client.list_objects(Bucket=bucket)
print(list_files)