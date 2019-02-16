from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Jxlv3ORZVdxP64nfCM48j0fnRZYLAMRTjXK3EG7hkSKzBgJt1VguLliLDk9bNnei2z6PQblB9bj8IqHY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'qetela',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SERVER_EMAIL = 'ngunyimacharia@gmail.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = (
    ('Ngunyi', 'ngunyimacharia@gmail.com'),
)

MANAGERS = (
    ('Ngunyi', 'ngunyimacharia@gmail.com'),
)
