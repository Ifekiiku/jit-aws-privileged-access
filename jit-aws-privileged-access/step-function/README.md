## This workflow will:

- Receive the request data from Lambda
- Wait for approval
- On approval, assume the JIT role using a Lambda function
- Return confirmation or denial
- Update the request status

## STEP FUNCTION - JIT ACCESS WORKFLOW

- Name: JITAccessApprovalWorkflow
- Type: Standard
- Choose "Author with code snippets"
- Runtime: Amazon States Language (JSON)
- Role: Create a role with permission to invoke all 3 Lambda functions

## NOTE
Replace "INPUT_THE_ARN_OF_YOUR_AssumeJITRoleFunction" in the code with your AssumeJITRoleFunction ARN
Also replace "INPUT_THE_ARN_OF_YOUR_UpdateAccessStatus" in the code with your UpdateAccessStatus ARN