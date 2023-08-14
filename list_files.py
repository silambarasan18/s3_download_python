import os
import boto3


#client
client = boto3.client('s3')

#path and other vars
bucket = 'billing-report-trial'
s3_prefix = 'billing-report-trial/trial/20230801-20230901/'

#list
# list_files = client.list_objects(Bucket=bucket)
# print(list_files)

response = client.list_objects_v2(Bucket=bucket, Prefix=s3_prefix)

# Process the response and retrieve object keys
if 'Contents' in response:
    object_keys = [obj['Key'] for obj in response['Contents']]
    print("Object keys inside prefix:")
    for key in object_keys:
        print(key)
else:
    print("No objects found in the specified prefix.")