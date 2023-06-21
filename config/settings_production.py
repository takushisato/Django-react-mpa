"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from .settings import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# 本番環境化
DEBUG = False
DJANGO_VITE_DEV_MODE = False

# collectstaticの結果を格納するディレクトリ
# また、今回はこのディレクトリより静的ファイルを配信します(config/urls.pyにて指定)
STATIC_ROOT = BASE_DIR / 'collected_static'

# 本番環境の場合、build.outDir と同じパスを指定する
DJANGO_VITE_ASSETS_PATH = BASE_DIR / 'frontend' / 'dist'
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]

# for django-cors-headers
CORS_ALLOWED_ORIGINS = []
