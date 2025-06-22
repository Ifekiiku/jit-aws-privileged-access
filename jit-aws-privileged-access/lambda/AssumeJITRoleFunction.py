import json
import boto3

sts = boto3.client('sts')

def lambda_handler(event, context):
    role_arn = event.get('roleArn')
    duration = int(event.get('duration', 3600))
    
    try:
        response = sts.assume_role(
            RoleArn=role_arn,
            RoleSessionName="JITSession",
            DurationSeconds=duration
        )

        creds = response['Credentials']
        creds['Expiration'] = creds['Expiration'].isoformat()


        return {
            'Credentials': {
                'AccessKeyId': creds['AccessKeyId'],
                'SecretAccessKey': creds['SecretAccessKey'],
                'SessionToken': creds['SessionToken'],
                'Expiration': creds['Expiration']
            }
        }    

    except Exception as e:
        return {
            'error': str(e),
            'status': 'FAILED'
        }
