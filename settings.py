# -*- coding: utf-8 -*-
import os

abs_path = lambda path: os.path.join(os.path.dirname(__file__), path)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('d1ffuz0r', 'd1fffuz0r@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'home',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS=True

USE_L10N = USE_I18N = False


MEDIA_ROOT = abs_path(os.path.join('public', 'site_media'))
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

STATIC_ROOT = abs_path('static') if not DEBUG else ''

STATICFILES_DIRS = (
    abs_path('static'),
)
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'c6pbe#!2ej8+^^bik^=m6bg2i^_*96_vtc)w5en$7wd=&6%zj4'

TEMPLATE_LOADERS = (
    'homesite.template_loaders.DjamlFilesystemLoader',
    'homesite.template_loaders.DjamlAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.csrf.middleware.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
    'homesite',
    'disqus',
    'django_masha',
    'gunicorn'
)

MASHA_CFG = {
    'selectable': 'post'
}
MASHA_JQEURY = True

DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = 'd1ffuz0rhomesite'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
