# Just-In-Time (JIT) Privileged Access Management on AWS

This project demonstrates a full-stack, real-world implementation of a JIT (Just-In-Time) IAM solution on AWS. It removes persistent admin privileges and enables controlled, time-limited elevated access. Built entirely using the AWS Console and Python Lambdas.

---

## 🚀 Features

- Request admin access securely via API
- Auto-approve mode for demos
- Issue temporary credentials using STS
- Record requests in DynamoDB
- Step Function handles the approval logic
- Optional TTL cleanup using DynamoDB TTL

---

## 🛠️ Tech Stack

- AWS Lambda (Python)
- API Gateway (secured with API key)
- DynamoDB (for request storage)
- Step Functions (approval workflow)
- STS (temporary access credentials)

---

## ⚙️ Setup Instructions

### 1. Create the IAM Elevated Role

- **Role Name**: `JIT-ElevatedAdminRole`
- **Trust Policy**:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::<your-account-id>:root" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- **Permissions**: Attach `AdministratorAccess` policy

---

### 2. Create DynamoDB Table

- **Table Name**: `JITAccessRequests`
- **Primary Key**: `requestId` (String)
- **TTL Attribute**: `expiresAt`

---

### 3. Create Lambda Functions

- **RequestElevatedAccess.py** (handles API calls and starts Step Function)
- **AssumeJITRole.py** (calls `sts:assumeRole` and returns temporary credentials)
- **UpdateAccessStatus.py** (updates request status in DynamoDB)

Each function should have its own IAM role with scoped permissions:

- `RequestElevatedAccess.py`: needs access to `dynamodb:PutItem`, `states:StartExecution`
- `AssumeJITRoleFunction.py`: needs `sts:AssumeRole`
- `UpdateAccessStatus.py`: needs `dynamodb:UpdateItem`

---

### 4. Create Step Function (Standard Workflow)

- Name: `JITAccessApprovalWorkflow`
- States:
  - SimulateApproval (Choice)
  - AssumeJITRole (Lambda task)
  - Approved / Denied (Lambda task)

Paste the definition from `step-function/state-machine.json`

---

### 5. Create REST API in API Gateway

- **Method**: POST `/request-access`
- **Integration**: Lambda (`RequestElevatedAccess.py`)
- **Enable API Key**: Yes
- **Add to Usage Plan**

Use `curl` or Git Bash to test:

```bash
curl -X POST https://<your-api-id>.execute-api.us-east-1.amazonaws.com/prod/request-access \
  -H "x-api-key: <your-api-key>" \
  -H "Content-Type: application/json" \
  --data-binary @- <<EOF
{
  "requester": "admin@example.com",
  "role": "JIT-ElevatedAdminRole",
  "roleArn": "arn:aws:iam::<account-id>:role/JIT-ElevatedAdminRole",
  "duration": 900,
  "simulateApproval": true
}
EOF
```

---

## 🧪 Testing Flow

1. Submit API request
2. Request is logged in DynamoDB
3. Step Function simulates approval
4. STS role is assumed (if approved)
5. Temporary credentials are returned
6. DynamoDB entry updated to `APPROVED`

---

## 🔄 Optional: Instant Credential Return with Express Workflow

To return credentials instantly:

- Re-create the Step Function as `Express`
- Use `start_sync_execution()` in `RequestElevatedAccess.py`
- Parse and return `response["output"]` as JSON

> ⚠️ This incurs additional AWS charges per invocation.

---

## 🏁 Final Notes

This project gives a real-world JIT access implementation that’s:

- Practical
- Secure
- Extendable (approval UI, email alerts, Slack notifications)

You can rebuild this from the AWS Console or automate it using Infrastructure as Code

---

**Author:** Ifekiiku Phillips – Cloud Architect & DevOps Educator

