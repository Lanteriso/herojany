"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import django_heroku
import os
from .base import *
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9qgh-%y9tr2*6cxvnzf8(u8a!&&&ea_-@-a18gooqunwozt)c$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#数据库设置

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
if os.getenv('DATABASE_URL') is not None:
    import dj_database_url

    DATABASES['default'] = dj_database_url.config()


# 发送邮件设置
# https://docs.djangoproject.com/en/2.0/ref/settings/#email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'lrnman@qq.com'
EMAIL_HOST_PASSWORD = 'umuxopsdpcgnbggf'#muzwogwhwqmrcaif'  # 授权码
EMAIL_SUBJECT_PREFIX = '[JANYROO BLOG] '
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
django_heroku.settings(locals())#这放结尾