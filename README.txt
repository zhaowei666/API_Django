Deployment:
$ ssh -i KEY-PEM-FILE ubuntu@EC2-ENDPOINT
$ git clone GITHUB-LINK
$ apt-get update
$ apt-get install python-pip python-dev build-essential
$ pip install --upgrade pip
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ vim mysite/settings.py
  Add endpoint to ALLOWED_HOSTS
$ python manage.py runserver


