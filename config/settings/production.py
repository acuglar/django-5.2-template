from .base import *


ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(',')
INTERNAL_IPS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', 'localhost'),
        'PORT': env('DB_PORT', '5432'),
        'CONN_MAX_AGE': 600,
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS
