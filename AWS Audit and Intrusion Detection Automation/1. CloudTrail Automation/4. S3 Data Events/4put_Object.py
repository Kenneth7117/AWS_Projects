import boto3
import time
import os

# Set up the AWS profile to use
profile = 'logging'

# Configure the session using the specified profile
session = boto3.Session(profile_name=profile)
sts_client = session.client('sts')
s3_client = session.client('s3')

# Create the content.txt file
content = "these are the pale deaths that men miscall their lives"
with open('content.txt', 'w') as file:
    file.write(content)

# Get the AWS account ID
response = sts_client.get_caller_identity()
account_id = response['Account']

# Generate a unique bucket name using the current timestamp
new_bucket = f"digdug-rutabaga-{int(time.time())}"

# Create the new S3 bucket
s3_client.create_bucket(Bucket=new_bucket)
print(f"Bucket '{new_bucket}' created successfully.")

# Upload the content.txt file to the newly created S3 bucket
s3_client.put_object(
    Bucket=new_bucket,
    Key=f"digdug-rutabaga-{account_id}",
    Body=open('content.txt', 'rb')
)
print(f"File 'content.txt' uploaded successfully to bucket '{new_bucket}'.")

# Optionally, clean up the file after uploading
os.remove('content.txt')
