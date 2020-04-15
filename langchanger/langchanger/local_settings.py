import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.1']

DEBUG = True

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
