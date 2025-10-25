#!/bin/bash
export DJANGO_SETTINGS_MODULE=config.settings.development
export ENV_FILE=.env.development

uv run manage.py runserver