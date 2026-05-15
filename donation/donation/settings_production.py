import os
import sys
import urllib.parse as urlparse

from django.core.exceptions import ImproperlyConfigured

from .settings import *  # noqa: F403, F401

# Override settings for production
DEBUG = False

# Security settings for production
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Allowed hosts for production deployment
ALLOWED_HOSTS = [
    '.onrender.com',
    '.railway.app',
    '.up.railway.app',
    '.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# Add custom domains from environment variables
if os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.getenv('RENDER_EXTERNAL_HOSTNAME'))
if os.getenv('RAILWAY_PUBLIC_DOMAIN'):
    ALLOWED_HOSTS.append(os.getenv('RAILWAY_PUBLIC_DOMAIN'))
if os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS.extend(
        [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h.strip()]
    )

# CSRF for HTTPS reverse proxies (Render, Railway, custom domains)
CSRF_TRUSTED_ORIGINS = []
_render_host = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if _render_host:
    CSRF_TRUSTED_ORIGINS.append(f'https://{_render_host}')
_railway = os.getenv('RAILWAY_PUBLIC_DOMAIN')
if _railway:
    CSRF_TRUSTED_ORIGINS.append(f'https://{_railway}')
if os.getenv('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS.extend(
        [o.strip() for o in os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',') if o.strip()]
    )

# Database configuration for production
database_url = os.getenv('DATABASE_URL', '').strip()
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

if database_url:
    url = urlparse.urlparse(database_url)
    port = url.port or 5432
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:] if url.path else '',
            'USER': url.username or '',
            'PASSWORD': url.password or '',
            'HOST': url.hostname or '',
            'PORT': str(port),
        }
    }
    if not DEBUG:
        DATABASES['default']['CONN_MAX_AGE'] = 600
        DATABASES['default']['OPTIONS'] = {'connect_timeout': 10}
elif 'collectstatic' in sys.argv:
    # Docker image build / CI: collectstatic does not need a real database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    raise ImproperlyConfigured(
        'DATABASE_URL must be set in production (use a free Postgres such as Neon or Supabase).'
    )

# Static files configuration for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ensure staticfiles directories exist
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

# Add whitenoise for static file serving
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Whitenoise settings (non-manifest avoids rare missing-map deploy failures)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Allow all file extensions for static files
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = False

# Email configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

# Site settings for production
SITE_DOMAIN = (
    os.getenv('RENDER_EXTERNAL_HOSTNAME')
    or os.getenv('RAILWAY_PUBLIC_DOMAIN')
    or os.getenv('SITE_DOMAIN')
    or 'localhost'
)
