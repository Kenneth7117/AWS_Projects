# STAGE 3 - Web Identity Federation

![Stage3 - PNG](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/Cognito(Stage3).png)  

# STAGE 3A - CREATE A COGNITO IDENTITY POOL  

Move to the Cognito Console https://console.aws.amazon.com/cognito/home?region=us-east-1#
On the menu on the left, select `Federated Identities`  
We're going to be creating a new identity pool  
If this is your first, the creation process will begin immediatly, if you already have any identity pools you'll have to click `federated identities` then click on `Create new identity pool`     
In `Identity pool name` enter `PetIDFIDPool`   
Expand `Authentication Providers` and click on `Google+`   
In the `Google Client ID` box, enter the Google Client ID you noted down in the previous step.  
Click `Create Pool`   

# STAGE 3B - Permissions  

Expand `View Details`    
This is going to create two IAM roles  
One for `Your authenticated identities` and another for your `Your unauthenticated identities`    
For now, we're just going to click on `Allow` we can review the roles later.    

You will be presented with your `Identity Pool ID`, note this down, you will need it later.
Click to move back to the dashboard  

# STAGE 3C - Adjust Permissions  

The serverless application is going to read images out of a private bucket created by the initial cloudformation template.    
The bucket is called `patchesprivatebucket`    
Move to the IAM Console https://console.aws.amazon.com/iam/home?region=us-east-1#/home    
Click `Roles`   
Locate and click on `Cognito_PetIDFIDPoolAuth_Role`  
Click on `Trust Relationships`  
See how this is assumable by `cognito-identity.amazonaws.com`  
With two conditions  
- `StringEquals` `cognito-identity.amazonaws.com:aud` `your congnito ID pool`  
- `ForAnyValue:StringLike` `cognito-identity.amazonaws.com:amr` `authenticated`  
This means to assume this role - you have to be authenticated by one of the ID providers defined in the cognito ID pool.    

When you use WEDIDF with cognito, this role is assumed on your behalf by cognito, and its what generates temporary AWS credentials which are used to access AWS resources.  

Click `permissions` .. this defines what these credentials can do.  

The cloudformation template created a managed policy which can access the `privatepatches` bucket
Click `Add permissions` and then `Attach policies`  
Type `PrivatePatches` in the search box and press `enter`  
Check the box next to `PrivatePatchesPermissions` and click `Attach Policies`    


# STAGE 3 - FINISH    

- template front end app bucket  
- Configured Google API Project  
- Credentials to access it  
- Cognito ID Pool  
- IAM Roles for the ID Pool  
