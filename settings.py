DATABASE_PASSWORD = ''
SECRET_KEY = ''
SECURITY_PASSWORD_HASH = ''
SECURITY_PASSWORD_SALT = ''
SECURITY_REGISTERABLE = ''

try:
   from dev_settings import *
except ImportError:
   pass