# Readme

#### Also enable all SQL Statement Log

- ref: https://docs.djangoproject.com/en/dev/topics/logging/
- ref: https://docs.djangoproject.com/en/dev/topics/logging/#django-db-backends

- if you add below configure in your settings.py

```
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
```

- and you can get below information

```
>>> book.models.Storage.objects.all()
(0.000) SELECT "book_storage"."id", "book_storage"."label", "book_storage"."description" FROM "book_storage"  LIMIT 21; args=()
<QuerySet [<Storage: Storage object (1)>, <Storage: Storage object (2)>]>
>>> 
```

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

#### Entering interactive console for your project, Test ORM Cache mechanism

- In same object instance or pointer, django will use cached data after secondary operation.

```
./manage.py shell
```

```
>>> import book.models
>>> qs = book.models.Storage.objects.all()

>>> print([row for p in qs]) # Evaluate the query set, retrieve from database directly
>>> print([row for p in qs]) # Re-use the cache from the evaluation without connect to database
```

![Alt text](https://raw.githubusercontent.com/scott1028/django-orm-cache-mechanism-study/master/orm-cache-mechanism.png "orm-cache-mechanism.png")
