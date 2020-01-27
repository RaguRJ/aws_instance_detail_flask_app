# Update and install pip3
sudo yum update -y
sudo yum install python3-pip -y
sudo yum install python-pip -y
sudo yum install git -y
sudo pip install --upgrade pip virtualenv
sudo amazon-linux-extras install epel -y
sudo yum install supervisor -y

# Account to own server process
sudo useradd -m -d /home/pythonapp pythonapp

# Fetch source code
export HOME=/root
sudo git clone https://github.com/RaguRJ/aws_instance_detail_flask_app.git /opt/app

# Supervisor configuration
sudo cp /opt/app/supervisord.conf /etc/supervisord.conf

# Python environment setup
sudo virtualenv -p python3 /opt/app/env
source /opt/app/env/bin/activate
sudo /opt/app/env/bin/pip install -r /opt/app/requirements.txt

# Set ownership to newly created account
sudo chown -R pythonapp:pythonapp /opt/app

# Put supervisor configuration in proper place
sudo cp /opt/app/python-app.conf /etc/supervisor.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update