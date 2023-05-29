
from pathlib import Path

from decouple import config
import os
import environ

from django import conf


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)
# Take environment variables from .env file
environ.Env.read_env(BASE_DIR/'.env')
# False if not in os.environ because of casting above
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['https://www.hydinsaudi.com/', 'https://web-production-8948.up.railway.app/','https://web-production-9ba7.up.railway.app','127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    "phonenumber_field",
    'django_countries',
    'sorl.thumbnail',
    'widget_tweaks',
    'django_filters',
    "django_htmx",
    "accounts",
    "categories",
    "expads",
    "vendor",
    "ads",
    "storages",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'expads.context_processors.menu_links',
                'accounts.context_processors.get_user_profile',                
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

""" 
DATABASES = {
    "default": {
        'ENGINE': env('ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        "PORT" : env("DB_PORT"),
    }
}
 """
AUTH_USER_MODEL = env('AUTH_USER_MODEL')

#STATICFILES_STORAGE= config('STATICFILES_STORAGE')
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT=BASE_DIR/'static'
STATICFILES_DIRS=['main/static']

STATIC_ROOT=os.path.join(BASE_DIR,"/static")
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Email configuration
GOOGLE_API_KEY = env('GOOGLE_API_KEY')
EMAIL_BACKEND=env('EMAIL_BACKEND')
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT', cast=int)
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
RZP_KEY_ID=env('RZP_KEY_ID')
RZP_KEY_SECRET=env('RZP_KEY_SECRET')
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

CSRF_COOKIE_SECURE=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
SESSION_COOKIE_SECURE=True
#USE_X_FORWARDED_HOST=True
#X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000 # > 6 months (197 days)
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
#DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME=env('AWS_S3_BUCKET_NAME')
AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE=env('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE=env('STATICFILES_STORAGE')
#AWS_S3_CUSTOM_DOMAIN=env('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#print(f"AWS_SECRET_ACCESS_KEY = {AWS_SECRET_ACCESS_KEY}")
DATABASES = {
    "default": {
        'ENGINE':env('ENGINE'),
        'NAME':env('DB_NAME'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'HOST':env('DB_HOST'),
        'PORT':'5432',
    }
}


""" # SITE SECURITY (security)
SECURE_SSL_REDIRECT = False
if DEBUG is False:
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    #USE_X_FORWARDED_HOST=True
    #X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000 # > 6 months (197 days)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    #DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_BUCKET_NAME=env('AWS_S3_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    DEFAULT_FILE_STORAGE=env('DEFAULT_FILE_STORAGE')
    STATICFILES_STORAGE=env('STATICFILES_STORAGE')
    #AWS_S3_CUSTOM_DOMAIN=env('AWS_S3_CUSTOM_DOMAIN')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    #print(f"AWS_SECRET_ACCESS_KEY = {AWS_SECRET_ACCESS_KEY}")
    DATABASES = {
        "default": {
            'ENGINE': env('ENGINE'),
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            "PORT": env("DB_PORT"),
        }
    }

else:
    SECURE_SSL_REDIRECT=False
    SESSION_COOKIE_SECURE=False
    CSRF_COOKIE_SECURE=False
    DATABASES = {
        "default": {
            'ENGINE': env('ENGINE'),
            'NAME': env('LDB_NAME'),
            'USER': env('LDB_USER'),
            'PASSWORD': env('LDB_PASSWORD'),
            'HOST': env('LDB_HOST'),
        }
    } """


#print(f"SECURE_SSL_REDIRECT = {SECURE_SSL_REDIRECT}")
#print(f"SECRET_KEY = {SECRET_KEY}")

#if DEBUG == True:
#    print('True')
#else:
#    print('False')

"""
# Following setting for http 
# python manage.py runserver 8080

DEBUG=True
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False
"""