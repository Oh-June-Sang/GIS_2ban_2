from .base import *

env_list = dict()

local_emv = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_emv.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=') # SECRET_KEY = 에서 "=" 위치
    key = line[:start] # SECRET_KEY = 전
    value = line[start+1:]  # SECRET_KEY = 다음
    env_list[key] = value
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env_list['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}