from .settings import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 第三方登錄網站ID
SITE_ID = 3
SOCIAL_AUTH_FACEBOOK_KEY = '512360503226187' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '93f933713f562da4c9ad22101a904e2a' # Facebook App Secret
