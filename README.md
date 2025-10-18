# Django 5.2 Documentation

# installation
```sh
mkdir <project_name> && cd <project_name>
uv init
uv add django==5.2
source .venv/bin/activate
django-admin startproject [config] .
uv run manage.py runserver # warning about unapplied database migrations
