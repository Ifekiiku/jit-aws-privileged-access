# 🔐 AWS Just-In-Time (JIT) Privileged Access Management

This project eliminates standing admin privileges using temporary role assumption via an approval workflow built entirely with AWS native services.

## 🧱 Architecture Overview

- IAM Identity Center for user identity
- Lambda for request processing and role assumption
- Step Functions for approval flow
- DynamoDB for audit logging
- STS for temporary role assumption

## 🚀 Features

- Request-driven elevated access
- Approval workflow with Step Functions
- Temporary credentials using STS
- Audit logs in DynamoDB
- Easily extensible (UI, email alerts, expiration cleanup)

See full documentation in the `/docs` folder.
