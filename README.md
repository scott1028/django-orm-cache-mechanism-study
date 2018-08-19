# Readme

#### Prerequisite

```
sudo apt install python3-dev libmysqlclient-dev
pip install mysqlclient
```

#### create project steps

```
virtualenv. venv -p python3
source .venv/bin/activate
```

```
django-admin startproject myApp ./
./manage.py startapp book 
```

- myApp/settings.py
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book',  # add your app of project if it has a models
]

```


```
./manage.py makemigrations
./manage.py migrate
# if you change model, you always need to run above two command. ex: rename model className in your project.
```

- Below is a optional step
```
# if you need a initial data for app of django, please take a look at https://docs.djangoproject.com/en/2.1/howto/initial-data/

# after you create fixturedata for initial data, you might wonder to load them. ex: ./manage.py loaddata book/fixtures/Storage.json
# manage.py loaddata <fixturename> [<fixturename>]
```
