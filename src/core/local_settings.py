from environs import Env

env = Env()
env.read_env('.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ADMINISTRATOR_NAME = env('ADMINISTRATOR_NAME')
ADMINISTRATOR_PASSWORD = env('ADMINISTRATOR_PASSWORD')
ADMINISTRATOR_MAILBOX = env('ADMINISTRATOR_MAILBOX')

ADMIN_PANEL_NAME = env('ADMIN_PANEL_NAME')
ADMIN_PANEL_PASSWORD = env('ADMIN_PANEL_PASSWORD')

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
