from .common import *
from ..secret import SECRET_KEY

SECRET_KEY = SECRET_KEY

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
