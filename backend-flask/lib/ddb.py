import boto3
import sys
from datetime import datetime, timedelta, timezone
import uuid
import os

class Ddb:
  def client():
    endpoint_url = os.getenv("AWS_ENDPOINT_URL")
    if endpoint_url:
      attrs = { 'endpoint_url': endpoint_url }
    else:
      attrs = {}
    dynamodb = boto3.client('dynamodb',**attrs)
    return dynamodb

def list_message_groups(client,my_user_uuid):
    table_name = 'cruddur-messages'
    query_params = {
        'TableName': table_name,
        'KeyConditionExpression': 'pk = :pkey',
        'ScanIndexForward': False,
        'Limit': 20,
        'ExpressionAttributeValues': {
            ':pkey': {'S': f"GRP#{my_user_uuid}"}
        }
    }
    print('query-params')
    print(query_params)
    print('client')
    print(client)