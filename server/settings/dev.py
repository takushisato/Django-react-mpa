# 開発環境用の設定

from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# for django-cors-headers
# CORS_ALLOWED_ORIGINS = (
#     'http://localhost:5173',
#     'http://127.0.0.1:5173',
# )

# templateで if debug を使えるようにするため、設定が必要
INTERNAL_IPS = (
    '127.0.0.1',
)
