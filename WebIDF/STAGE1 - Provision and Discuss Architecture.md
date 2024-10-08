# STAGE 1 - Web Identity Federation

![Stage1 - PNG](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/Cognito(Stage1).png) 

# STAGE 1A - Login to an AWS Account    

Login to the AWS account using a user with admin privileges and ensure your region is set to `us-east-1` `N. Virginia`  
Click [HERE](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/aws-cognito-web-identity-federation/WEBIDF.yaml&stackName=WEBIDF) to auto configure the infrastructure the app requires 
Check the  `The following resource(s) require capabilities: [AWS::IAM::ManagedPolicy, AWS::IAM::Role]` box  
Click `Create Stack`  

Wait for the STACK to move into the `CREATE_COMPLETE` state before continuing.  

# STAGE 1B - Verify S3 bucket  

Open the S3 console https://s3.console.aws.amazon.com/s3/home?region=us-east-1    
Open the bucket starting `webidf-appbucket`   
It should have objects within it, including `index.html` and `scripts.js`  
Click the `Permissions` Tab  
Verify `Block all public access` is set to `Off`  
Click `Bucket Policy`  
Verify there is a bucket policy  

# STAGE 1C - Verify privatebucket
Open the bucket starting `webidf-patchesprivatebucket-`  
Load the objects in the bucket so you are aware of the contents  
Verify there is no bucket policy and the bucket is entirely private.  

# STAGE 1D - Verify CloudFormation Distribution  

Move to the `CloudFront` consle https://us-east-1.console.aws.amazon.com/cloudfront/v3/home?region=us-east-1#/distributions  
Locate the distribution pointing at origin `webidf-appbucket-....`  and click  
Locate the `distribution domain name`  
Note down as the `WebApp URL` this name prefixed with https i.e if yours is `d1o4f0w1ew0exo.cloudfront.net` then your `WebApp URL` is `https://https://d1o4f0w1ew0exo.cloudfront.net` (note, the copy icon may copy the https:// for you)  

# STAGE 1 - FINISH  
At this stage you have the base infrastructure in place including:-

- front end app bucket
- privatepatches bucket  
- CloudFront distribution proving caching and HTTPS capability

In stage 2 you will create a google API project which will be the `ID Provider` for this serverless application.  
