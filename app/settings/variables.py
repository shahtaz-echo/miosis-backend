import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("APP_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("APP_ENV") == 'dev'

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]