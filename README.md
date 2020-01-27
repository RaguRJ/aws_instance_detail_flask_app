# AWS Instance meta-data Flask app

This is a pet project I have been working on. The objective is to enable an Amazon Linux 2 Instance to spin up a web app that displays all the (non-sensitive) EC2 instance meta-data information. I beleive this will be useful for people working on labs with Load balancers, cloud routing orchestration, containers (not tested yet) etc. where by making a http request to the instance IP would spit out all the details which will make sure troubleshooting or trying to understand the laod-balancing or traffic distribution of a cloud setup a little bit easier. To make this process repeatable, reusable and fast I have used startup scripts and supervisor process control more instructions below.

__tl;dr__ : Add the text in "aws_linux_2_ami_script.sh" in user instance metadata when deploying the instance and try accessing http://<public-ip>:8080 on a web-browser to view the instance metadata.


## Getting Started - Startup script

Follow the instructions below to set-up the web app for your instances.

### Prerequisites and constraints

* Tested on Amazon Linux 2 - amzn2-ami-hvm-2.0.20191217.0-x86_64-gp2 (ami-062f7200baf2fa504)
* If running on an instance without any Load Balancers - please make sure the instance is in a public subnet with a Internet-gateway setup
* If running on any other setup, make sure the instance is listening on HTTP Port 8080 and that the instance is reachable.
* All other requirements will be installed as part of the requirements.txt and the startup script

### Installing

* Copy the text form the [startup script](https://github.com/RaguRJ/aws_instance_detail_flask_app/blob/master/aws_linux_2_ami_script.sh) and paste it as a user data while deploying the instance
* The startup process takes while to complete (3-5 mins), after the initializing phase is complete open the following link in a browser "http://<Instance-IP>":8080

## Deploying and running app on a running instance

* If you are trying to run this app on an instance that is deployed and running, simply run the following commands on your instance

```
# Update and install pip3
sudo yum update -y
sudo yum install python3-pip -y
sudo yum install python-pip -y
sudo yum install git -y

# Cloning git repo 
sudo git clone https://github.com/RaguRJ/aws_instance_detail_flask_app.git /opt/app
cd /opt/app
sudo pip3 install -r requirements.txt

#Running the app
sudo python3 main.py
```
__Note:__ This method does not configure supervisor process control to run the app in the background or automatically start the app in case of a reboot. Plese refere to [startup script](https://github.com/RaguRJ/aws_instance_detail_flask_app/blob/master/aws_linux_2_ami_script.sh) to configure supervisor. Also, dont forget to add sudo when running the startup script commands on your instance.

## Disclaimer
* The instance meta-data server in aws http//:169.254.169.254/latest/meta-data/ has sensitive inforamtion under /identity-credentials/ and /public-keys/ paths. The [main.py](https://github.com/RaguRJ/aws_instance_detail_flask_app/blob/master/main.py) removes these sensitive information using the following code

```
# Deleting sensitive information from the dictionary
del path_dict["meta-data/"]["identity-credentials/"]
del path_dict["meta-data/"]["public-keys/"]
```

If you are absolutely sure and want to include these information in the web-app, comment out or remove the above lines from your code.


## Authors
* Ragu Jayaraman - [RaguRJ](https://github.com/RaguRJ)

## Acknowledgements and references
* https://tn710617.github.io/supervisor/
* https://cloud.google.com/python/tutorials/getting-started-on-compute-engine
* https://medium.com/@sureshamk/supervisor-in-centos-rhel-fedora-ca0288fa235
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
* A handful of stackoverflow python questions and other python/flask documentation