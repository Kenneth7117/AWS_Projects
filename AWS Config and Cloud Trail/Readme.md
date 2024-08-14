Introduction

(https://github.com/Kenneth7117/AWS_Projects/blob/main/AWS%20Config%20and%20Cloud%20Trail/Images/CloudTrail_and_Config_Lab.png)

In this hands-on lab, you just started as a Cloud Engineer at a company. Your new boss has asked you to do a scream test and stop an EC2 instance as well as remove network routes and rules to validate if the Lab VPC and Corporate Server EC2 instance can be decommissioned.

Very soon after the changes, the scream test fails and clients are reporting they cannot connect to their applications. Your boss reaches back out to you and asks you to revert all changes you made. In this lab, you will leverage AWS CloudTrail and AWS Config to ensure all changes are accounted for and reverted to restore the Lab environment. By the end of this exercise, you will be familiar enough with CloudTrail and Config to audit any unexpected or accidental changes to an account and determine what specifically was updated in case you need to roll back the changes.

Solution
Log in to the live AWS environment using the credentials provided. Make sure you are in the N. Virginia (us-east-1) region throughout the lab.

Initiate the Scream Test
Make sure you are in the N. Virginia region in the top right-hand corner of the console.
Navigate to the EC2 console by entering "EC2" in the search bar on top and selecting EC2 from the search results.
Locate the CorporateServer instance and select the checkbox next to instance. Make a note of the instance ID for later on in this lab.
Click on Instance state.
From the dropdown menu, click on Stop instance.
When prompted, click Stop.
In the Details tab below, click on the blue link under Subnet ID.
In the new browser tab or window that opens, select the PrivateAZ1 subnet. Make sure to note the route table ID for later on in this lab.
In the Details tab below, click on the blue link under Route table.
In the new browser tab or window that opens, click on the Routes tab below.
Click on Edit routes.
For the route with the following destination 0.0.0.0/0 and target nat-xxxxxxxxxxxxxxxxx, click on Remove next to the route for the NAT gateway.
Click on Save changes.
In the left-hand navigation menu, click on Security Groups under Security.
Locate and select the CorporateApplicationServer security group. Make sure to note the security group ID for later on in this lab.
Click on the Outbound rules tab below.
Click on Edit outbound rules.
Click on Delete for the one outbound rule with the destination set to 0.0.0.0/0.
Click on save rules.
Review the Changes for the Scream Test in Config and CloudTrail
Navigate to CloudTrail by entering "cloudtrail" in the search bar and selecting CloudTrail from the search results.
Click on the hamburger menu icon (the icon with three horizontal bars) in the top left corner.
Click on Event History.
Click on the Read-only dropdown menu and select Resource Name.
In the search field, paste in the Instance ID noted in the first step and look for the StopInstances event.
Select the StopInstances event and review the details of the change.
In the search field of the CloudTrail console, paste in the route table ID that you made note of before and look for any DeleteRoute events.
Select the DeleteRoute event and review the details of the changes.
At the bottom of the event details, click on View AWS Config resource timeline.
In the AWS Config timeline, you will see a Configuration change event at the very top. Click on the + icon to see the details of the changes.
Make note of the output in the JSON diff results, which show exactly what route from the PrivateAZ1 route table was deleted, specifically the NAT Gateway ID. You will need this later on in the lab.
In the search field of the CloudTrail console, paste in the Security Group ID noted in the first step and look for any RevokeSecurityGroupEgress events.
Select the RevokeSecurityGroupEgress event and review the details of the changes.
At the bottom of the event details, click on View AWS Config resource timeline.
Make note of the output in the JSON diff results, which show exactly what security group rules were deleted from the Corporate Application Server security group.
Revert the Scream Test Changes and Test Networking
Navigate to the VPC console by entering "VPC" in the search bar on top and selecting the VPC search result.

Click on Security Groups.

Locate and select the CorporateApplicationServer security group.

Click on the Outbound rules tab, and click on Edit outbound rules.

Select Add rule and set the following values:

Type: Select All Traffic.
Destination: Select Anywhere-IPv4.
Click on Save rules to complete reverting the security group change.

In the left-hand navigation menu, click on Route Tables.

Locate and select the PrivateAZ1RT route table.

Click on the Routes tab and click on Edit routes.

Select Add route and set the following values:

Destination: Enter "0.0.0.0/0".
Target: Select NAT Gateway.
Click on Save changes to complete reverting the route table change.

Navigate to the EC2 console by entering "EC2" in the search bar on top and select EC2 from the search results.

In the left-hand navigation menu, select Instances.

Find the CorporateServer instance.

Select the instance and click on Instance state.

Click on Start instance. You will need to wait a few minutes for the instance to fully boot back up and initialize.

Select the CorporateServer instance and click on Connect.

Click on the Session Manager tab and click on Connect.

Elevate your permission to the root user on the instance:

sudo -i
Run the following command to verify network connectivity:

yum install -y nmap
Run a ping test to a Google-resolving DNS server to confirm that we can reach out to the public internet:

ping -c4 8.8.8.8
Conclusion
Congratulations — you've completed this hands-on lab!
