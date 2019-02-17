import os,json
from .base import *


with open(os.path.abspath("qetela/secrets.json")) as f:
    secrets = json.loads(f.read())


def get_secret_setting(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': get_secret_setting('DATABASE_ENGINE'),
        'NAME': get_secret_setting('DATABASE_NAME'),
    }
}

STATIC_ROOT = 'static'

EMAIL_HOST_USER = get_secret_setting('EMAIL_HOST_USER')
EMAIL_HOST = get_secret_setting('EMAIL_HOST')
EMAIL_HOST_PASSWORD = get_secret_setting('EMAIL_HOST_PASSWORD')
EMAIL_PORT = get_secret_setting('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'ngunyimachariagmail.com'
SERVER_EMAIL = 'ngunyimachariagmail.com'

ADMINS = (
    ('Ngunyi', 'ngunyimachariagmail.com'),
)

MANAGERS = (
    ('Ngunyi', 'ngunyimachariagmail.com'),
)
