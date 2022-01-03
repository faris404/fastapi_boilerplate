import os

class Settings:

   DEBUG = True
   TITLE = 'hello'
   VERSION = '0.0.1'
   DESCRIPTION = 'testing'

   HOST = 'localhost'
   PORT = ''

   BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
   TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
   STATIC_DIR = os.path.join(BASE_DIR,'static')
   STATIC_URL = '/static'

   DATABASE_URL = f'sqlite://{BASE_DIR}/test.db'
   REDIS_URL = ''

   SECRET_KEY = '3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf'  # openssl rand -hex 32
   
   JWT_ALGORITHM = 'HS25'
   JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 day

   EMAIL = ''
   SMTP_USER = ''
   SMTP_HOST = 'smtp.gmail.com'
   SMTP_PORT = 587
   SMTP_TLS = True
   SMTP_PASSWORD = ''

   CORS_ORIGINS = [
      "http://localhost",
      "http://localhost:8080",
      "http://localhost:5000",
      "http://localhost:3000",
   ]
   CORS_ALLOW_CREDENTIALS = True
   CORS_ALLOW_METHODS = ["*"]
   CORS_ALLOW_HEADERS = ["*"]

   LOG_LEVEL = 'DEBUG'
   PRODUCTION_LOG_FILE = os.path.join(BASE_DIR,'production.log')
   DEBUG_LOG_FILE = os.path.join(BASE_DIR,'debug.log')
   LOG_HANDLERS = ['debug'] # ['production', 'debug']


settings = Settings()


loggerSettings = {
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
      'default': {
         'format': '[%(levelname)s]:[%(name)s]: %(message)s '
                     '(%(asctime)s; %(filename)s:%(lineno)d)',
         'datefmt': "%Y-%m-%d %H:%M:%S",
      },
   },
   'handlers': {
      'production': {
         'level': 'INFO',
         'class': 'logging.handlers.RotatingFileHandler',
         'filename': settings.PRODUCTION_LOG_FILE,
         'maxBytes': 1024 * 1024 * 10,
         'backupCount': 10,
         'formatter': 'default',
      },
      'debug': {
         'level': 'DEBUG',
         'class': 'logging.handlers.RotatingFileHandler',
         'filename': settings.DEBUG_LOG_FILE,
         'mode':'a',
         'maxBytes': 1024 * 1024 * 10,
         'backupCount': 10,
         'formatter': 'default',
      },
   },
   'loggers': {
      '': {
         'handlers': settings.LOG_HANDLERS,
         'level': settings.LOG_LEVEL,
      },
   }
}