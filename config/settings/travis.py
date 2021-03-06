from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='t2KINdlLtd2mkPeDbdeAHjR5cbZMVvADiMUHOaJUeCDDsvRuazAWslm5T')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'travisdb',
        'USER':     'postgres',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}
# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'localhost'
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025