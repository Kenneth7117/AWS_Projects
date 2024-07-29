# Web Identity Federation

In this Project we have implemented a serverless application which uses Web Identity Federation. Credits to Adrian Cantrill for his implementation.
The application runs using the following technologies

- S3 for front-end application hosting
- Google API Project as an ID Provider
- Cognito and IAM Roles to swap Google Token for AWS credentials

The application runs from a browser, gets the user to login using a Google ID and then loads all images from a private S3 bucket into a browser using presignedURLs.

This project consists of 5 stages :-

- STAGE 1 : Provision the environment and review tasks 
- STAGE 2 : Create Google API Project & Client ID
- STAGE 3 : Create Cognito Identity Pool
- STAGE 4 : Update App Bucket & Test Application
- STAGE 5 : Cleanup the account

## Instructions

- [Stage1](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/STAGE1%20-%20Provision%20and%20Discuss%20Architecture.md)
- [Stage2](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/STAGE2%20-%20Create%20Google%20APIProject%20and%20Client%20ID.md)
- [Stage3](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/STAGE3%20-%20Create%20Cognito%20Identity%20Pool.md)
- [Stage4](https://github.com/Kenneth7117/AWS_Projects/blob/main/WebIDF/STAGE4%20-%20Update%20App%20Bucket%20and%20Test%20Application.md)
