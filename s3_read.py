import json
import boto3
from decimal import Decimal
import pandas as pd

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='',
aws_secret_access_key=''
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

#Creating Object From the S3 Resource.   
obj = s3.Object('s3outputuser', 'e7bd231ee200459a844e45987c7a8b33829fe1b96bc15cd1a541717fb34c366d_0.json')


#Reading the File as String With Encoding
file_content = obj.get()['Body'].read().decode('utf-8') 

json_data = json.loads(file_content)

df = pd.json_normalize(json_data)

print(df)