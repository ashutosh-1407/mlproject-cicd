## End to End MAchine Learning Project

1. Docker Build checked
2. Github Workflow
3. IAM User In AWS

## Docker Setup In EC2 commands to be Executed

#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:

## Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

# To push larger files:

git config --global http.postBuffer 524288000  # 500MB

git config --global http.maxRequestBuffer 100M

# Other settings

# If Conda auto-activates (base), you can disable it:

conda config --set auto_activate_base false

# setting PYTHONPATH

export PYTHONPATH=$PYTHONPATH:/path/to/mlproject-cicd
