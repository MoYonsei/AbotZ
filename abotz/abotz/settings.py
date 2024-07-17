"""
Django settings for abotz project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from django.middleware.security import SecurityMiddleware
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8k1eev7@epo47z@003lv$p@a(_4#m5pl!q45w1pii#gm*+s^i5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'yourdomain.com', '10.0.2.2']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'user_accounts.apps.UserAccountsConfig',
    'bots.apps.BotsConfig',
    'crispy_forms',
    'rest_framework',
    'corsheaders',
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'abotz.urls'

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

WSGI_APPLICATION = 'abotz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abotz',       # اسم قاعدة البيانات التي أنشأتها
        'USER': 'root',             # اسم المستخدم الافتراضي لـ XAMPP
        'PASSWORD': '',             # اترك كلمة المرور فارغة إذا لم تقم بتعيينها
        'HOST': 'localhost',        # المضيف (localhost لـ XAMPP)
        'PORT': '3306',             # منفذ MySQL الافتراضي
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Set the default language code
LANGUAGE_CODE = 'en'

# Define the available languages
LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
    # Add other languages here
]

# Set the path for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'

STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'user_accounts.CustomUser'

LOGIN_URL = '/user_accounts/login'
LOGIN_REDIRECT_URL = '/bots/bots_list'


CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5555',
    'http://10.0.2.2:5555'
]
CSP_DEFAULT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]
CSP_IMG_SRC = ["'self'", 'data:']
CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'"]
CSP_FRAME_SRC = ["'self'", 'http://127.0.0.1:5555', 'http://10.0.2.2:5555']
CSP_FRAME_ANCESTORS = ["'self'", 'http://127.0.0.1:5555', 'http://10.0.2.2:5555']

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'ALLOW-FROM http://127.0.0.1:5555'


