from .base import *


ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(',')
INTERNAL_IPS = ['127.0.0.1','localhost']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
