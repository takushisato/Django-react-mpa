# 本番環境用設定

from .base import *


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# 本番環境化
DEBUG = False
DJANGO_VITE_DEV_MODE = False

# collectstaticの結果を格納するディレクトリ
# また、今回はこのディレクトリより静的ファイルを配信します(server/urls.pyにて指定)
STATIC_ROOT = BASE_DIR / 'collected_static'

# 本番環境の場合、build.outDir と同じパスを指定する
DJANGO_VITE_ASSETS_PATH = BASE_DIR / 'frontend' / 'dist'
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]

# for django-cors-headers
CORS_ALLOWED_ORIGINS = []
