import os
import boto3


#client
client = boto3.client('s3')

#path and other vars
bucket = 'billing-report-trial'
cur_path = os.getcwd()
file = '124522506816-aws-cost-allocation-AISPL-2023-08.csv'
filename = os.path.join(cur_path, 'downloads', file)

#object_method to download file
client.download_file(
    Bucket = bucket,
    Key=file,
    Filename=filename
)

#list the contents of DL dir
download_dir = os.path.join(cur_path, 'downloads')

for root, dirs, files in os.walk(download_dir):
    for fn in files:
        print(fn)
