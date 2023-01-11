import boto3

aws_access_key_id='',
aws_secret_access_key='',
region_name='us-east-1'
s3 = boto3.client('s3')

def get_s3_keys(bucket):
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])

    return keys

if __name__=="__main__":
    key_is = get_s3_keys('s3outputuser')
    print(key_is)
