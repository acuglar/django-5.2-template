#!/bin/bash
export DJANGO_SETTINGS_MODULE=config.settings.production
export ENV_FILE=.env

gunicorn config.wsgi:application