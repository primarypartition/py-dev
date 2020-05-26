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


### projct server

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

