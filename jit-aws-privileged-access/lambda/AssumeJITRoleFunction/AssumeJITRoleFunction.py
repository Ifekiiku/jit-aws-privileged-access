import boto3
import json
import os
from datetime import datetime

def lambda_handler(event, context):
    sts = boto3.client('sts')
    role_arn = event['roleArn']
    duration = event['duration']

    assumed_role = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="JITSession",
        DurationSeconds=duration
    )

    creds = assumed_role['Credentials']
    return {
        "Credentials": {
            "AccessKeyId": creds['AccessKeyId'],
            "SecretAccessKey": creds['SecretAccessKey'],
            "SessionToken": creds['SessionToken'],
            "Expiration": creds['Expiration'].isoformat()
        }
    }