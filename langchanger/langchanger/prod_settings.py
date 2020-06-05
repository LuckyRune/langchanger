import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIR = os.path.join(BASE_DIR, 'langchanger-vue')

ALLOWED_HOSTS = ['test-d-v.herokuapp.com']

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = True

BOT_TOKEN = os.environ.get('TG_BOT')

STATIC_ROOT = os.path.join(FRONTEND_DIR, 'dist')

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

