# Create DynamoDB Table

- Name: JITAccessRequests
- Partition Key: requestId (String)
- Enable TTL:
    TTL Attribute: <expiresAt>
        This will automatically delete expired access records