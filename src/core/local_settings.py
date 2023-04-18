from environs import Env

env = Env()
env.read_env('.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ADMINISTRATOR_NAME = env('ADMINISTRATOR_NAME')
ADMINISTRATOR_PASSWORD = env('ADMINISTRATOR_PASSWORD')
ADMINISTRATOR_MAILBOX = env('ADMINISTRATOR_MAILBOX')

POST_SERVER_NAME = env('POST_SERVER_NAME')
POST_SERVER_PORT = env('POST_SERVER_PORT')
SERVICE_MAILBOX = env('SERVICE_MAILBOX')
SERVICE_MAILBOX_PASSWORD = env('SERVICE_MAILBOX_PASSWORD')

ADMIN_PANEL_NAME = env('ADMIN_PANEL_NAME')
ADMIN_PANEL_PASSWORD = env('ADMIN_PANEL_PASSWORD')
