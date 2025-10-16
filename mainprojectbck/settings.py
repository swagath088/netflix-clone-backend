from pathlib import Path
import os
import dj_database_url

# ----------------------
# Paths
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# Security
# ----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # or you can put your domains

# ----------------------
# Installed Apps
# ----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'mainapp.apps.MainappConfig',

    'cloudinary',
    'cloudinary_storage',
]

# ----------------------
# Middleware
# ----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------
# URLs & Templates
# ----------------------
ROOT_URLCONF = 'mainprojectbck.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainprojectbck.wsgi.application'

# ----------------------
# Database
# ----------------------
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# ----------------------
# Password Validators
# ----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------
# Internationalization
# ----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------
# Static & Media Files
# ----------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cloudinary setup
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# ----------------------
# REST Framework
# ----------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

# ----------------------
# CORS Settings
# ----------------------
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://netflix-clone-django-react.vercel.app",
    "https://netflix-clone-django-react-swagaths-projects.vercel.app",
    "https://netflix-clone-backend-1-4ynr.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://netflix-clone-django-react.vercel.app",
    "https://netflix-clone-django-react-swagaths-projects.vercel.app",
    "https://netflix-clone-backend-1-4ynr.onrender.com",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
