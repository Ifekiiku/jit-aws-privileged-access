## Create the Elevated Role

- Name: JIT-ElevatedAdminRole
- Type: IAM Role
- Trusted entity: Another AWS principal (IAM roles or users)

## Trust Policy
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": { "AWS": "arn:aws:iam::<account-id>:root" },
        "Action": "sts:AssumeRole"
        }
    ]
    }

## Permssions

- Attach AdministratorAccess (or scoped down version if required)