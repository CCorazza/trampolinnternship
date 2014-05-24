# Django settings for my project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = 'ccorazza@student.42.fr'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ccorazza@student.42.fr'
EMAIL_HOST_PASSWORD = 'mCKb0ss4815162342'
EMAIL_PORT = 468
EMAIL_USE_TLS = True

ADMINS = (
    (u'root', 'ccorazza@student.42.fr')
)
MANAGERS = ADMINS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'


### ------------------------------ Internationalization ------------------------------

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

### ------------------------------------- Apps ---------------------------------------

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'landingpage',
)

BOOTSTRAP3 = {
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.0.3/',
    'css_url': None,
    'theme_url': None,
    'javascript_url': None,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
)

### ------------------------------- Templates & URLs -------------------------------


ROOT_URLCONF = 'internship.urls'

WSGI_APPLICATION = 'internship.wsgi.application'

TEMPLATE_DIRS = (
    BASE_DIR+'/templates',
    BASE_DIR+'/app/templates',
    )

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "conf/locale"),
]

### ------------------------------------ Logging ------------------------------------

SECRET_KEY = 'xtjyxthw6^k0d&9xomxu(=@&zg6ji-bs&i-&ss2(021n4%zll+'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR + '/db.conf',
        },
    }
}
