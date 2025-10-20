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

### models best practices
- Add `__str__` method to models for better representation in admin and shell
- Specify `related_name` for reverse relationships
- Use custom model methods for common queries
- Use `@classmethod` for model-level operations

### django admin site
1. create superuser: `uv run manage.py createsuperuser`
2. register models in polls.admin
3. access http://localhost:8000/admin/

## templates
1. create directory polls/templates/polls/
2. create template index.html
3. create view to render template
4. map view to url in polls.urls

### views best practices
- Whenever you create a form that alters data server-side, use `method="post"`
- Since we’re creating a POST form, we need to include the `{% csrf_token %}` template tag inside the `<form>` element

## Tests
- test save time
- Tests don’t just identify problems, they prevent them
- Tests make code more attractive
- When testing, more is better

1. create polls test in polls.tests
2. `uv run manage.py test`

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

## Static files
1. create directory polls/static/polls/
2. create style.css in polls/static/polls/
3. add link to stylesheet in template