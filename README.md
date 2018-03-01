#Django backend
This Django project provides RESTful API support to my website</br>
(ec2-18-217-239-185.us-east-2.compute.amazonaws.com)

##Installation and deployment:
#####Clone Github repo
`git clone https://github.com/zhaowei666/API_Django.git`
#####Install pip
`apt-get update`
`apt-get install python-pip python-dev build-essential`
#####Install virtualenv
`pip install --upgrade pip`
`pip install virtualenv`
#####Initialize virtualenv
`virtualenv env`
`source env/bin/activate`
#####Install libraries
`pip install -r requirements.txt`
#####Update database
`python manage.py makemigrations`
`python manage.py migrate`
#####Open setting file add endpoint to ALLOWED_HOSTS
`vim mysite/settings.py` 
#####Run
`python manage.py runserver`
#####If deployed in AWS, use
`python manage.py runserver 0.0.0.0:80`

