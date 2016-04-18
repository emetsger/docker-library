# -*- coding: utf-8 -*-
'''Example settings/local.py file.
These settings override what's in website/settings/defaults.py

NOTE: local.py will not be added to source control.
'''

from . import defaults

# DOMAIN = 'https://test.osf.io/''
# API_DOMAIN = 'https://test-api.osf.io/'

DEV_MODE = True
DEBUG_MODE = True  # Sets app to debug mode, turns off template caching, etc.

ELASTIC_URI = 'elasticsearch'
SEARCH_ENGINE = 'elastic'
ELASTIC_TIMEOUT = 10

DB_HOST = 'tokumx'

# LOG_PATH = '/log'

# Comment out to use SHARE in development
USE_SHARE = False

# Comment out to use celery in development
USE_CELERY = False

# Comment out to use GnuPG in development
USE_GNUPG = False  # Changing this may require you to re-enter encrypted fields

# Email
USE_EMAIL = False
MAIL_SERVER = 'localhost:1025'  # For local testing
MAIL_USERNAME = 'osf-smtp'
MAIL_PASSWORD = 'CHANGEME'

# Mailchimp email subscriptions
ENABLE_EMAIL_SUBSCRIPTIONS = False

# Session
OSF_COOKIE_DOMAIN = None
COOKIE_NAME = 'osf'
SECRET_KEY = "CHANGEME"

# Uncomment if GPG was installed with homebrew
# GNUPG_BINARY = '/usr/local/bin/gpg'

##### Celery #####
## Default RabbitMQ broker
BROKER_URL = 'amqp://rabbitmq'

# Default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://rabbitmq'

USE_CDN_FOR_CLIENT_LIBS = False

# Example of extending default settings
# defaults.IMG_FMTS += ["pdf"]

CAS_SERVER_URL = 'http://192.168.99.100:8080'
DOMAIN = 'http://192.168.99.100:5000/'
API_DOMAIN = 'http://192.168.99.100:8000/'
WATERBUTLER_URL = 'http://192.168.99.100:7777'
WATERBUTLER_ADDRS = ['192.168.99.100']
#DB_HOST = '172.17.0.2'
#ELASTIC_URI = '172.17.0.3:9200'
