## API GATEWAY SETTINGS

- Create a REST API (not HTTP API)
- Resource: /request-access
- Method: POST
- Integration: Lambda → RequestElevatedAccess
- Deploy the API
- Add API Key + Usage Plan
- Secure with x-api-key header

## 🔐 Example Test via Git Bash:
    curl -X POST https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/request-access \
    -H "x-api-key: <your-api-key>" \
    -H "Content-Type: application/json" \
    --data-binary @- <<EOF
    {
    "requester": "admin@ifekiiku.com",
    "role": "JIT-ElevatedAdminRole",
    "roleArn": "arn:aws:iam::<account-id>:role/JIT-ElevatedAdminRole",
    "duration": 900,
    "simulateApproval": true
    }
    EOF

## NOTE
# Replace the following in the 'Example test' code
- <api-id>
- <your-api-key>
- <account-id>