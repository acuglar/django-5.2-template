# Django 5.2 Documentation

## installation
```sh
mkdir <project_name> && cd <project_name>
uv init
uv add django==5.2
source .venv/bin/activate
django-admin startproject [config] .
uv run manage.py runserver # warning about unapplied database migrations
```
http://localhost:8000/

## create app polls
```sh
uv run manage.py startapp polls
```
### 1. configure urls
1. ./polls/urls.py
2. ./config/urls.py
### 2. create view
1. ./polls/views.py
http://localhost:8000/polls/ 