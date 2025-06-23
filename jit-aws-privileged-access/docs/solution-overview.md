## 🔍 Industry Problem Statement

Most enterprises operating in AWS environments suffer from excessive standing privileges and poor access governance. Common issues include:
- Users/roles with long-term AdministratorAccess or broad policies.
- No centralized visibility into “who can do what”.
- Temporary or ex-employee accounts left active.
- Difficulty enforcing Least Privilege across multiple AWS accounts.
- Inconsistent use of identity federation or SSO.
- No automated way to expire or audit temporary elevated access.

## 💡 Project Solution Summary

This solution provides a Just-In-Time (JIT) Access Management Framework with:
- Centralized Identity Federation via IAM Identity Center (SSO).
- Role-based access control with permission sets.
- Temporary privilege elevation (JIT access) using IAM Roles and AWS Lambda workflows.
- Approval-based access using AWS Step Functions and EventBridge.
- Audit logging with CloudTrail and centralized access insights in AWS Config.

It enforces Zero Standing Privileges by ensuring users only have access when absolutely needed — and only for a limited time — after being approved.

## 🧱 High-Level Architecture

- IAM Identity Center (SSO) integrated with external IdP (e.g., Azure AD or Okta).
- Permission Sets assigned per group (e.g., Developers, Auditors, Admins).
- JIT Access Flow:
    - User requests elevated access via a portal (API Gateway + Lambda).
    - Request triggers Step Functions with approval logic.
    - On approval, STS issues temporary role credentials.
    - Access expires automatically.
- Audit Logging: CloudTrail + AWS Config + custom Lambda for tagging/logging actions.
- Security Guardrails: SCPs and IAM Policy boundaries prevent privilege escalation.

## 🛠️ Tech Stack

| Service                 | Purpose                              |
| ----------------------- | ------------------------------------ |
| **IAM Identity Center** | Centralized SSO & permission sets    |
| **IAM Roles**           | Temporary privilege assignment       |
| **STS**                 | Temporary security credentials       |
| **AWS Lambda**          | Custom workflows and logic           |
| **AWS Step Functions**  | Approval flow for JIT access         |
| **CloudTrail**          | Auditing access and changes          |
| **EventBridge**         | Triggering workflows based on events |
| **DynamoDB**            | Track access request logs            |
| **S3**                  | Archive logs and policies            |
