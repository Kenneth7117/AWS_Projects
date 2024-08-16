# Using Docker Bench to Enhance Container Security

- Gain access to the EC2 CentOS7 server through the terminal of your choice using ssh to log in as cloud_user.
```
$ ssh cloud_user@[Public IP Here]
```
- Clone the docker-bench repo from github.com:
```
$ git clone https://github.com/docker/docker-bench-security.git
```
- Change your present working directory to docker-bench-security:
```
$ cd docker-bench-security
```
- Using superuser permissions execute the docker-bench-security.sh shell script and redirect standard output to a file called /tmp/bench1.out
```
$ sudo sh docker-bench-security.sh > /tmp/bench1.out
```
- *The sudo command will prompt your for the cloud_user password
- **NOTE**: At this point, you may get warnings or errors.
- This is ok, and expected, as the checks are always being updated, please proceed to check the output file created from this command.
- Use the more command to look at the first part of the docker bench output:
```
$ more /tmp/bench1.out
```

![Bench1](https://github.com/Kenneth7117/AWS_Projects/blob/main/Docker%20Bench/Images/Screenshot%202024-08-16%20110207.png)

- Use the auditctl command to list any auditing rules that are already setup on the system:
```
$ sudo auditctl -l
```
- Use the auditctl command to add a rule to audit the /var/lib/docker directory:
```
$ sudo auditctl -w /var/lib/docker -k "docker lib"
```
- Now run the docker bench utility again and direct output to /tmp/bench2.out:
```
$ sudo sh docker-bench-security.sh > /tmp/bench2.out
```
- Now use the Linux diff command to compare the output from the first run in bench1.out to the second run in bench2.out:
```
$ diff /tmp/bench1.out /tmp/bench2.out
```

![Bench2](https://github.com/Kenneth7117/AWS_Projects/blob/main/Docker%20Bench/Images/Screenshot%202024-08-16%20110947.png)
