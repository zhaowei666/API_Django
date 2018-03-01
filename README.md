#Django backend
This Django project provides RESTful API support to my website</br>
(ec2-18-217-239-185.us-east-2.compute.amazonaws.com)

##Installation and deployment:
`git clone GITHUB-LINK`</br>
`apt-get update`</br>
`apt-get install python-pip python-dev build-essential`</br>
`pip install --upgrade pip`</br>
`pip install virtualenv`</br>
`virtualenv env`</br>
`source env/bin/activate`</br>
`pip install -r requirements.txt`</br>
`python manage.py makemigrations`</br>
`python manage.py migrate`</br>
`vim mysite/settings.py` #Add endpoint to ALLOWED_HOSTS</br>
`python manage.py runserver`</br>
If deployed in AWS, use `python manage.py runserver 0.0.0.0:80`</br> 

