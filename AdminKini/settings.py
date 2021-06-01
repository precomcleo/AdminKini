import os

'''
基本配置
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'tglidezx#yx784&=yvpchw3v5bygqhuzx-75+w)bow#64+ged2'

DEBUG = True
ALLOWED_HOSTS = ['*']

'''
App
'''
# Application definition
INSTALLED_APPS = [
    'base',
    'pages',
    'Commodity',
    'Order',
    'UploadFile',
    'Vendor',
    'WechatBot',
    'Wedding',
    'Portfolio',
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',          #彈窗警告
    'django.contrib.staticfiles',
    # excel
    'import_export',
    # 第三方登入 social-auth-app-django
    'social_django',
    # 第三方登入 django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',
    # WechatScheduler
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',                #i18n
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',   #第三方登入social-auth-app-django
]

ROOT_URLCONF = 'AdminKini.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',              #i18n
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #第三方登入social-auth-app-django
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'AdminKini.wsgi.application'

'''
Database
'''
import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# GCP正式環境
if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/kinihouse-project:asia-east2:django',
            'USER': 'root',
            'PASSWORD': 'Aa123456',
            'NAME': 'djangodb',
        }
    }
# GCP開啟雲端連線
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'djangodb',
            'USER': 'root',
            'PASSWORD': 'Aa123456',
        }
    }
# 開發本地runserver
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }

'''
多語系
'''
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True

# 網站可支持的語言
from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ('en', _('English')),   #python manage.py makemessages -l en_US
    ('zh-hans', _('Simplified Chinese')), #python manage.py makemessages -l zh_Hant
    ('zh-hant', _('Traditional Chinese')), #python manage.py makemessages -l zh_Hans
)

# 設置翻譯檔 locale 的路徑
PROJECT_ROOT = os.path.dirname(os.path.realpath(__name__))
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

'''
第三方登錄 (共用)
'''
# 設置登入的方式
AUTHENTICATION_BACKENDS = (
    # 第三方登入 django-allauth
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    # 第三方登入 social-auth-app-django
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
)

# --第三方登錄 (django-allauth)--
# 第三方登錄網站ID
SITE_ID = 3

# 登入登出導向
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/home'

# google 登入
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }

# --第三方登錄 (social-auth-app-django)--
# 登入登出導向
#LOGIN_URL = '/'
#LOGOUT_URL = '/'
#LOGIN_REDIRECT_URL = '/'

# 第三方的 KEY 和 SECRET (**DEV)
SOCIAL_AUTH_FACEBOOK_KEY = '153618330010446' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '5e80a0b5e9e458c89fa91dfe5113e6ad' # Facebook App Secret

'''
安全性
'''
# 密碼驗證
AUTH_PASSWORD_VALIDATORS = [
    # 用户属性相似验证，检查密码和一组用户的属性的相似性
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    # 最小长度验证，最小接受长度为 5
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    'OPTIONS': {'min_length': 5,}},
    # 常见密码验证，这个检查器会对比常用的弱密码，这些常用密码被 gzip 打包储存在 `django/contrib/auth/common-passwords.txt.gz` 中 
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    # 纯数字密码验证
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

'''
靜態檔路徑(CSS, JavaScript, Images)
'''
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

'''
其他
'''
# excel
IMPORT_EXPORT_USE_TRANSACTIONS = True