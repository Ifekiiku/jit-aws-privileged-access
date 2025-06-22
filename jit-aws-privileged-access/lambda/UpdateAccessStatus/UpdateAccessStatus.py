import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = "JITAccessRequests"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    request_id = event['requestId']
    status = event['status']

    table.update_item(
        Key={"requestId": request_id},
        UpdateExpression="SET #s = :s",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":s": status}
    )
    return {"message": f"Request {request_id} updated to {status}"}