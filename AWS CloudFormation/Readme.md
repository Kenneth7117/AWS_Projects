# AWS Cloud Formation
## Introduction
Your development team has been using this template for the intern-testing program. After performing an analysis, your team has determined that the t3.small instance was more compute power than they needed. Update the template so that the default instance defined in the stack is a t3.micro.

In this hands-on lab, we're going to jump into an environment that already has a CloudFormation stack deployed. We'll review the contents of the CloudFormation template, and then we'll perform direct updates to the stack itself.

## Solution
- Log in to the AWS Management Console using the credentials provided on the lab instructions page. Make sure you're using the us-east-1 region.
### Using Application Composer, Configure the InstanceType Stack Parameter to T3.Micro
- In the search bar at the top, enter "CloudFormation".
- Select CloudFormation from the dropdown menu.
- Select the stack already in the CloudFormation dashboard.
- Review the Stack info tab.
- Review the Events tab (the newest events will appear first).
- Review the Resources tab.
- Right-click and open the physical ID for the InternetGateway in a new tab.
- Right-click and open the physical ID for the WebServerInstance in a new tab.
- Close out the InternetGateway and WebServerInstance tabs after reviewing.
- Review the Outputs tab.
- Right-click on the PublicDNS link and open it in a new tab. (Make sure to specify http, not https).
- Navigate back to the CloudFormation dashboard.
- Click on the Parameters tab.
- Near the top of the page, next to Delete, click Update.
- Ensure Use current template is selected and click Next.
- Under InstanceType, select t3.micro.
- Note: This only changes the current deployment of the stack.
- Click Cancel.
- Navigate back to the CloudFormation dashboard and click on the existing stack.
- Click Update again.
- Select Edit in Application Composer and click Edit in Application Composer.

![Application Composer](https://github.com/Kenneth7117/AWS_Projects/blob/main/AWS%20CloudFormation/Images/Screenshot%202024-08-16%20001027.png)

- Click the Template view at the top.

![Template View](https://github.com/Kenneth7117/AWS_Projects/blob/main/AWS%20CloudFormation/Images/Screenshot%202024-08-16%20001135.png)

- Ensure YAML is selected for the template.
- Under Parameters, change the default size from t3.small to t3.micro by erasing "small" and typing "micro".
### Launch the Updated Stack and Verify the New EC2 Resource Is Reachable
- Click Validate.
- Click Update template.
- Note: This is a direct update to the existing stack.
- Click Confirm and continue to CloudFormation.
- Click Next.
- Under Parameters, select the InstanceType dropdown box and select t3.micro.
- Click Next and Next.
- Scroll down and select the acknowledgement under Capabilities.
- Click Submit.
- Click on the refresh icon in the top-right corner of the CloudFormation dashboard to ensure the update is complete (this may take a few minutes).
- Navigate to the Resources tab and open the WebServerInstance physical ID in a new tab to verify that the InstanceType is t3.micro.
- Navigate back to the CloudFormation dashboard and select the Outputs tab.
- Open the PublicDNS value in a new tab to ensure the instance is reachable via the public web.
## Conclusion
- Hands on knowledge on the working of Cloud Formation.
- Using Application Composer for Canvas/Template View
- Applying modifications and changes to the template parameters
