import os
from decouple import config

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='mydb'),
        'USER': config('DB_USER', default='myuser'),
        'PASSWORD': config('DB_PASSWORD', default='mypassword'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://localhost:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Other settings (SECRET_KEY, DEBUG, etc.)
SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)
USE_I18N=config('USE_I18N', default=True, cast=bool)
ROOT_URLCONF='adapters.django.urls'
