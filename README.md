# Python Project


## Projects


### HTML, CSS, Bootstrap

> https://codepen.io/primarypartition/project/editor/ZOgQbR

> https://codepen.io/primarypartition/pen/jObXbEO

> https://github.com/primarypartition/sample-website/tree/master/gallery


### JavaScript, DOM

> https://codepen.io/primarypartition/pen/rNOoLZG

> https://codepen.io/primarypartition/pen/WNQLpBz


### JQuery

> https://codepen.io/primarypartition/pen/GRpPEPb


### Django Basic Project

> https://py-dev-first-project.herokuapp.com/
 
 
### Django Blog

> https://py-dev-blog.herokuapp.com/

 
### Django Social

> https://py-dev-social.herokuapp.com


## Python 3.6 install

> sudo add-apt-repository ppa:jonathonf/python-3.6

> sudo apt-get update

> sudo apt-get upgrade

> sudo apt-get install python3.6

> python3 --version


## Install conda

> https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

> wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

> bash Anaconda3-2020.02-Linux-x86_64.sh

```
conda -V
conda list
```


## Create virtual environment

> https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

```
conda env list
conda info --envs

conda deactivate
conda activate base

conda create --name mydjenv django
conda activate mydjenv
```


## Django install

> conda activate mydjenv

> conda install django


## Django project

> django-admin startproject first_project


### Projct server

> python manage.py runserver

> python manage.py runserver 192.168.33.100:8000


### Update settings.py 

```
ALLOWED_HOSTS = ['192.168.33.100']
```


### Create Django application

```
python manage.py startapp first_app
```

> register app with project through settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'first_app'
]
```


## Faker Lib

```
pip install Faker
```


## DB migration

```
> python manage.py migrate

> python manage.py makemigrations first_app

> python manage.py migrate

> python manage.py migrate first_app
```


## Django Commands

```
conda env list
conda info --envs

conda deactivate
conda activate base

conda create --name mydjenv django
conda activate mydjenv

> django-admin startproject first_project

> python manage.py runserver

> python manage.py runserver 192.168.33.100:8000

> python manage.py startapp home_app

> python manage.py migrate

> python manage.py makemigrations first_app

> python manage.py migrate

> python manage.py createsuperuser

> python manage.py shell
```


## Django DB

```
from first_app.models import Topic

Topic(top_name="Lorem")
Topic(top_name="Mauris")
Topic(top_name="Integer")
Topic(top_name="Aenean")

t = Topic(top_name="Lorem")
t.save()
t = Topic(top_name="Mauris")
t.save()
t = Topic(top_name="Integer")
t.save()
t = Topic(top_name="Aenean")
t.save()

Topic.objects.all()
```


## Freeze project

```
pip freeze > requirements.txt
```


## Django Deployment

> https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

> https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps

> https://devcenter.heroku.com/articles/deploying-python

> https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html


### Heroku


> https://github.com/heroku/django-heroku

> https://devcenter.heroku.com/articles/django-assets

> https://devcenter.heroku.com/articles/deploying-python

```
pip install django_heroku
pip install dj-database-url gunicorn whitenoise
```


> In settings.py

```
ALLOWED_HOSTS = ['192.168.33.100', 'py-dev-first-project.herokuapp.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

at the very bottom:

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```


> In Procfile

```
web: gunicorn first_project.wsgi --log-file -
```


> Project deployment

```
pip freeze > requirements.txt

heroku login -i
heroku create app_name

git init 
git remote add heroku git@heroku
git add .
git commit -m "project"
git push heroku master

heroku ps:scale web=1

heroku run python manage.py migrate
heroku run python manage.py makemigrations first_app
heroku run python manage.py migrate

heroku run python manage.py createsuperuser
heroku run python seed.py
heroku run python seed_user.py

heroku config:set DISABLE_COLLECTSTATIC=1 
```


## Encryption


```
pip install bcrypt

pip install django[bcrypt]

pip install django[argon2]
```


### In settings.py

> https://docs.djangoproject.com/en/3.0/topics/auth/passwords/

```
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':9}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```


## Image upload

```
pip install pillow 
Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
```


## Django Debug

> https://github.com/jazzband/django-debug-toolbar

```
pip install django-debug-toolbar
```


> https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

> settings.py

```
INTERNAL_IPS = [
    # ...
    '192.168.33.100',
    # ...
]

INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]

MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

```

> urls.py

```
from django.conf import settings
from django.urls import include

if settings.DEBUG:
  import debug_toolbar

  urlpatterns = [path('__debug__', include(debug_toolbar.urls)),] + urlpatterns
```


## Django admin customization 


> https://github.com/django/django

> https://github.com/django/django/tree/master/django/contrib/admin/templates


```
in project_root

mkdir templates

in templates

mkdir admin

follow director structure as in github repo

django -> contrib -> admin -> templates -> admin

touch base_site.html

customize it as per requirements

in project settings.py mst register templates directory
```
