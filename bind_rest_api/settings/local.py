from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1+2n=+k$nh47+3b4@chg9-(0rp2-()8e*_fcm2rx&q19gxp01='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'named',
    'USER': 'root',
    'PASSWORD': 'vagrant',
    'HOST': 'localhost',
    'OPTIONS': {
        'sql_mode': 'STRICT_TRANS_TABLES',
    }
}

TIME_ZONE = 'America/Chicago'

ALLOWED_HOSTS.append('*')

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = []
REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = []
