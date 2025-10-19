# Django 5.2 Documentation

## installation
1. `mkdir <project_name> && cd <project_name>`
2. `uv init`
3. `uv add django==5.2`
4. `source .venv/bin/activate`
5. `django-admin startproject [config] .`
6. `uv run manage.py runserver` # warning about unapplied database migrations
7. access http://localhost:8000/

## create app polls
1. `uv run manage.py startapp polls`
2. `touch polls/urls.py`
3. add polls urls to config.urls
4. create view in polls.views
5. access http://localhost:8000/polls/

## database setup

### create app models
1. `uv run manage.py migrate`
2. create polls model in polls.models 
3. add app polls to config.settings.INSTALLED_APPS
4. `uv run manage.py makemigrations polls`
5. `uv run manage.py migrate`
6. `uv run manage.py sqlmigrate polls 0001`

### [interact with database via shell](/tuto/django_shell.md)
1. `uv run manage.py shell`

### models good practice
- Add `__str__` method to models for better representation in admin and shell
- Specify `related_name` for reverse relationships
- Use custom model methods for common queries
- Use `@classmethod` for model-level operations

### django admin site
1. create superuser: `uv run manage.py createsuperuser`
2. register models in polls.admin
3. access http://localhost:8000/admin/