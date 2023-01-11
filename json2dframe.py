import json
import boto3
from decimal import Decimal
import pandas as pd

file_path = "textract_output.json"

def read_json_data(file_path):
    data = []
    with open(file_path) as f:
        data = json.loads(f.read())
        print(type(data))
        print(len(data))
    return data[:300]

if __name__ == "__main__":
    data = read_json_data(file_path=file_path)
    df = pd.json_normalize(data)
    print(df)
