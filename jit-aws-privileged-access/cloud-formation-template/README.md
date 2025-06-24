# AWS CloudFormation Template for Just-In-Time (JIT) Privileged Access Management

This is the **CloudFormation (CFN) template** for deploying the full infrastructure behind the Just-In-Time Privileged Access Management system on AWS. It automates the creation of all necessary AWS resources required to request, approve, and assume privileged roles dynamically and securely.

---

## 🚀 What This Template Deploys

- **Amazon DynamoDB** – Stores access requests with TTL (auto-expiry).
- **AWS Lambda Functions** – Handle request submission, role assumption, and status updates.
- **AWS Step Functions** – Orchestrates the JIT access approval workflow.
- **API Gateway** – Provides a secure HTTP endpoint for initiating access requests.
- **IAM Roles and Policies** – For secure execution permissions across all components.

---

## 🛠️ Use Cases

This CloudFormation template is designed to support:

- 🔐 **Zero standing privileges** in your AWS environment  
- ⏱️ **Time-bound access** with auto-expiring credentials  
- 🧑‍💻 **Just-in-time elevation** for developers, engineers, or admins  
- 📜 **Audit-friendly workflows** with full request tracking  
- 🧩 **Easy integration** with identity providers or approval UIs  
- 🚧 **Testing & Simulation** support (via `simulateApproval` flag)

---

## 📦 How to Use

1. Deploy the CloudFormation stack via the AWS Console or CLI:
   ```bash
   aws cloudformation deploy \
     --template-file jit-access.yaml \
     --stack-name JITAccessStack \
     --capabilities CAPABILITY_NAMED_IAM

## Testing API Gateway
- Once deployed, you can test it from Git Bash or Postman using the URL:
    ```bash
    curl -X POST https://API_ID.execute-api.REGION.amazonaws.com/prod/request-access \
        -H "Content-Type: application/json" \
        -d '{
          "requester": "admin@ifekiiku.com",
          "role": "JIT-ElevatedAdminRole",
          "roleArn": "arn:aws:iam::ACCOUNT_ID:role/JIT-ElevatedAdminRole",
          "duration": 900,
          "simulateApproval": true
        }'
    ```

- Watch the Step Function execution to see approval flow in action.
