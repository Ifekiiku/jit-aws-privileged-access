import json
import boto3
import uuid
from datetime import datetime

stepfunctions = boto3.client('stepfunctions')
dynamodb = boto3.resource('dynamodb')

STATE_MACHINE_ARN = "arn:aws:states:us-east-1:701785833185:stateMachine:JITAccessApprovalWorkflow"
TABLE_NAME = "JITAccessRequests"

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # Debugging

    # Handle both API Gateway and direct invocation
    if "body" in event:
        try:
            body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid JSON body"})
            }
    else:
        body = event  # Direct invocation (e.g., from Lambda test)

    try:
        request_id = str(uuid.uuid4())
        requester = body["requester"]
        role = body["role"]
        role_arn = body["roleArn"]
        duration = int(body["duration"])
        simulate_approval = body.get("simulateApproval", False)
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": f"Missing required field: {str(e)}"})
        }

    # Save request to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "requestId": request_id,
            "requester": requester,
            "role": role,
            "status": "PENDING",
            "requestedAt": datetime.utcnow().isoformat(),
            "duration": duration
        }
    )

    # Start Step Function execution asynchronously
    try:
        response = stepfunctions.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=json.dumps({
                "requestId": request_id,
                "requester": requester,
                "role": role,
                "roleArn": role_arn,
                "duration": duration,
                "simulateApproval": simulate_approval
            })
        )
        print("Step Function started:", response)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Failed to start Step Function execution",
                "error": str(e)
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Access request submitted",
            "requestId": request_id,
            "executionArn": response["executionArn"]
        })
    }
