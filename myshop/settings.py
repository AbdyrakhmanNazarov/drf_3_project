from pathlib import Path
import environ
from decouple import config
from celery.schedules import crontab
import json

BASE_DIR = Path(__file__).resolve().parent.parent

# Настройка env
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(BASE_DIR / '.env')

# Основные настройки
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ["*"]

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'rest_framework',
    'drf_yasg',
    'django_resized',

    'accounts',
    'product',
    'django_celery_beat',  # обязательно для beat
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs и шаблоны
ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Модель пользователя
AUTH_USER_MODEL = 'accounts.User'

CORS_ALLOWED_ORIGINS = json.loads(config("CORS_ALLOWED_ORIGINS"))
CORS_ALLOWED_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRES_DB'),
#         'USER': env('POSTGRES_USER'),
#         'PASSWORD': env('POSTGRES_PASSWORD'),
#         'HOST': env('POSTGRES_HOST'),
#         'PORT': env('POSTGRES_PORT'),
#     }
# }

# Язык и часовой пояс
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True

# REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Celery настройки
CELERY_BROKER_URL = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/0"
CELERY_RESULT_BACKEND = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/0"

# Celery Beat - периодическая задача
CELERY_BEAT_SCHEDULE = {
    'delete-expired-otps-every-5-min': {
        'task': 'accounts.tasks.delete_expired_otps',
        'schedule': 300.0,  # каждые 5 минут
    },
}

# Статика и медиа
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
