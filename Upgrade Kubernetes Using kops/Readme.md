# Upgrade Kubernetes Using kops
## Introduction
This lab guides students through the creation of a cluster using kops, then upgrading the Kubernetes version by editing the cluster configuration and performing a rolling update. This terminates and then re-instantiates the master node and each of the worker nodes.
Students use kops to create the cluster and the kops editory (vi) to edit parameters in the kops cluster configurations file.
Github repository: https://raw.githubusercontent.com/ACloudGuru-Resources/content-kubernetes-security-ac/master/nginx179.yaml

## Solution
- Log into the server using the credentials provided for the lab.
ssh cloud_user@<PUBLIC_IP_ADDRESS>
### Create the Cluster
- After logging into the server, run the ls -l command.
```
$ ls -l
```
- The script required to create the cluster displays. Run the script to create a cluster.
```
$ . ./k8s-create.sh
```
- After the script runs, use the kops edit cluster command to view the Kubernetes version. Your Kubernetes version may vary from the version shown in the lab video.
```
$ kops edit cluster
```
- Run the :q! command at the end of the script to exit edit mode.
- Run the kops update cluster command to instantiate the cluster. This typically takes 5-10 minutes. You can log into the AWS Console and view the EC2 Instances to ensure the servers are being created.
```
$ kops update cluster --yes
```
- Run the kops validate cluster command to verify the DNS status. If the DNS is still spinning up, you receive a validation failure. The following command runs for 10 minutes until the cluster is ready.
```
$ kops validate cluster --wait 10m
```
- When the cluster is ready, run the kubectl get nodes command. This shows the node details, including the Kubernetes version.
```
$ kubectl get nodes
```
- Run the kubectl apply command with full the GitHub file URL.
```
$ kubectl apply -f https://raw.githubusercontent.com/ACloudGuru-Resources/content-kubernetes-security-ac/master/nginx179.yaml
```
- Run the kubectl get pods command until all the replica servers show a Status of Running.
```
$ kubectl get pods
```
### Update the Kubernetes Version

- Use the kops edit cluster command to edit the cluster configuration file.
```
$ kops edit cluster
```
- Scroll down to the kubernetesVersion line and change the version to 1.18.3, which is supported by kops in the lab environment.
- Run the kops update cluster command to update the cluster.
```
$ kops update cluster --yes
```
- Run the kops rolling-update command to perform rolling updates. This allows you to manage updates for all your worker nodes without downtime.
```
$ kops rolling-update cluster --validation-timeout 30m --yes
```
- Each node is cordoned (or cornered off) so no workloads can be deployed to it. After a node is cordoned, the system waits and eventually terminates the node instance, then a new node is re-instantiated. You may watch the cluster update from the AWS console as it terminates and re-instantiates nodes.
- If you are in a high availability environment with multiple master and worker nodes, ensure there are no outages when you perform this type of upgrade.
- After the rolling update is complete, run the kubectl get nodes command to confirm the Kubernetes version is correct.
```
$ kubectl get nodes
```
- Run the kubectl get pods command to confirm the replica servers are running.
```
$ kubectl get pods
```
## Conclusion
Congratulations — you've completed this hands-on lab!
