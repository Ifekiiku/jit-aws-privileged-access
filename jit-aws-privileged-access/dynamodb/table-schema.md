## Create DynamoDB Table

- Name: JITAccessRequests
- Partition Key: requestId (String)
- Enable TTL:
    TTL Attribute: expiresAt
        This will automatically delete expired access records

## 📝 Table Structure (Simple Version)

| Attribute     | Type   | Description                                       |
| ------------- | ------ | ------------------------------------------------- |
| `requestId`   | String | Unique ID (UUID) for each request                 |
| `requester`   | String | Email/username of requester                       |
| `role`        | String | Role being requested (e.g. JIT-ElevatedAdminRole) |
| `status`      | String | `PENDING`, `APPROVED`, etc.                       |
| `requestedAt` | String | Timestamp of request                              |
| `duration`    | Number | Access duration in minutes                        |
