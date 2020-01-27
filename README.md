# AWS Instance meta-data Flask app

This is a pet project I have been working on. The objective is to enable an Amazon Linux 2 Instance to spin up a web app that displays all the (non-sensitive) EC2 instance meta-data information. I beleive this will be useful for people working on labs with Load balancers, cloud routing orchestration, containers (not tested yet) etc. where by making a http request to the instance IP would spit out all the details which will make sure troubleshooting or trying to understand the laod-balancing or traffic distribution of a cloud setup a little bit easier. To make this process repeatable, reusable and fast I have used startup scripts and supervisor process control more instructions below.

tl;dr : Add the text in "aws_linux_2_ami_script.sh" in user instance metadata when deploying the instance and try accessing http://<public-ip>:8080 on a web-browser to view the instance metadata.
