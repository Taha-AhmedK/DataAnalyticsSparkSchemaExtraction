from pathlib import Path
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ca9k4wp1@b73f60fxs78_odw^re0_t#l6@_ts28ne-6^yy&ppb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'http://206.72.205.105:8081',
    'http://206.72.205.105',
    '206.72.205.105',
    'localhost',
    'http://74.50.81.184:9072/',
    'http://74.50.81.184',
    '74.50.81.184',
    '158.220.114.235',
    '5.189.150.186',
    'http://206.72.205.105:8070/',
    '144.126.140.238',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'extract',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'channels.middleware.WebSocketMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8050',
    'http://127.0.0.1:5500',
    'http://206.72.205.105:3000',
    'http://206.72.205.105:8070',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002',
    'http://localhost:3003',
    'http://localhost:3004',
    'http://localhost:3005',
    'http://74.50.81.184:3000',
    'http://74.50.81.184:3001',
    'http://74.50.81.184:8070'
]

CORS_ALLOWED_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'schema_extraction_app.urls'

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

WSGI_APPLICATION = 'schema_extraction_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Uncomment whichever file directory you need to set and comment the other one
# with open('/root/dataanalytics/services/XtremeAnalyticsConfig/app_config.json', 'r') as config_file:
# with open(
#     "/mnt/d/InnovativeSolutions/DataAnalytics/DataAnalyticsDataTransformation/app/app_config.json",
#     "r",
# ) as config_file:
# with open('/root/xtremeanalytix/XtremeAnalytixConfig/config.json', 'r') as config_file:    
#     config_data = json.load(config_file)
#     SERVER_IP = config_data['default_server_ip']
#     SPRING_SERVICES_PORT = config_data['microservices_port']
#     DJANGO_SERVICE_PORT = config_data['transformation_port']
#     DJANGO_SERVER_IP = config_data['transformation_server_ip']

# 74.50.81.184 - 9072 - 9052
# 206.72.205.105 - 9072 - 8081

# Production Server
# SERVER_IP = '74.50.81.184'
# SPRING_SERVICES_PORT = '9072'
# DJANGO_SERVICE_PORT = '9052'
# Development Server
# SERVER_IP = '206.72.205.105'
# SPRING_SERVICES_PORT = '9072'
# DJANGO_SERVICE_PORT = '8081'

# SPRING_ADMIN_SERVICES_URL = f'http://{SERVER_IP}:{SPRING_SERVICES_PORT}/registration/v1/'
# SPRING_SERVICES_URL = f'http://{SERVER_IP}:{SPRING_SERVICES_PORT}/dataanalytics/v1/'
# DJANGO_SPARK_INTERFACE_URL = f'http://{DJANGO_SERVER_IP}:{DJANGO_SERVICE_PORT}/data-retrieval-by-query-app/test-query'
# DJANGO_SERVICES_URL = f'http://{DJANGO_SERVER_IP}:{DJANGO_SERVICE_PORT}/data-reader/get-source-data/'


# Local Taha
# Please add your local directories paths ( Taha & Shabbir )
# AH Local Server Config
# DATA_STORE_PATH = 'D:/InnovativeSolutions/DataAnalyticsProduction/DATA_STORE'

# For Production
# DATA_STORE_PATH = ''
# ML_MODEL_PATH = '/Innovativesolutions/Dataanalytics/data/Healthcare_Studies/The_Innovative_Sol/CLINICAL_TRAIL_PRODUCT_EFFICACY/MLModels/'
# ML_MODEL_PREDICTION_PATH = ''


# DATA_STORE_PATH = "/mnt/d/InnovativeSolutions/DataAnalytics"
# ML_MODEL_PATH = '/mnt/d/InnovativeSolutions/DataAnalytics/Innovativesolutions/Dataanalytics/data/Healthcare_Studies/The_Innovative_Sol/CLINICAL_TRAIL_PRODUCT_EFFICACY/MLModels/'
# ML_MODEL_PREDICTION_PATH = '/mnt/d/InnovativeSolutions/DataAnalytics'
