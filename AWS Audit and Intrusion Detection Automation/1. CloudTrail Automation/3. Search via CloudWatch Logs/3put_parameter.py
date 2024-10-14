import boto3

# Define the AWS profile
profile = 'logging'

# Create a session using the specified profile
session = boto3.Session(profile_name=profile)

# Get the AWS account ID
sts_client = session.client('sts')
account_id = sts_client.get_caller_identity()['Account']

# Create an SSM client
ssm_client = session.client('ssm')

# Put a parameter into the AWS SSM Parameter Store
parameter_name = f'CeleryStalks{account_id}'
parameter_value = f'the celery stalks at midnight - {account_id}'

ssm_client.put_parameter(
    Name=parameter_name,
    Value=parameter_value,
    Type='String',
    Overwrite=True
)

print(f'Successfully stored parameter {parameter_name} with value "{parameter_value}"')
