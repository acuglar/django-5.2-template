"""
Django settings for config project.
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from django.contrib.messages import constants
from django.contrib.messages import constants as messages
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

ENV_FILE = env('ENV_FILE', default=None)
if ENV_FILE:
    environ.Env.read_env(ENV_FILE)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default='True')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'debug_toolbar',
    'corsheaders',
]
PROJECT_APPS = [
    'server.core',
    'server.polls',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # django-debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # django-cors-headers
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # django-requestlogs
    'requestlogs.middleware.RequestIdMiddleware',
    'requestlogs.middleware.RequestLogsMiddleware',

    # custom middleware
    'server.core.middleware.RequestTimingMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'client' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #custom context processors
                'server.core.context_processors.global_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'client' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',
}

LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'requestlogs.log',
        },
        'root': {
            'class': 'logging.StreamHandler',
            'filters': ['request_id_context'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['root'],
            'level': 'INFO',
        },
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'filters': {
        'request_id_context': {
            '()': 'requestlogs.logging.RequestIdContext',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(request_id)s %(module)s:%(lineno)s %(message)s'
        },
    },
}

REQUESTLOGS = {
    'STORAGE_CLASS': 'requestlogs.storages.LoggingStorage',
    'ENTRY_CLASS': 'requestlogs.entries.RequestLogEntry',
    'SERIALIZER_CLASS': 'requestlogs.storages.BaseEntrySerializer',
    'SECRETS': ['password', 'token'],
    'ATTRIBUTE_NAME': '_requestlog',
    'METHODS': ('GET', 'PUT', 'PATCH', 'POST', 'DELETE'),
    'JSON_ENSURE_ASCII': True,
    'IGNORE_USER_FIELD': None,
    'IGNORE_USERS': [],
    'IGNORE_PATHS': None,
}

# Config Messages
# MESSAGE_LEVEL = messages.DEBUG
MESSAGE_TAGS = {
	# messages.DEBUG: 'alert-danger',
	messages.INFO: 'alert-info',
	messages.SUCCESS: 'alert-success',
	messages.WARNING: 'alert-warning',
	messages.ERROR: 'alert-danger',
}
