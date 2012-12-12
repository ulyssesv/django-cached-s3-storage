# coding: utf-8

from setuptools import setup

setup(name='django-cached-s3-storage',
      version='0.1',
      author='Ulysses V',
      author_email='uvilela@inoa.com.br',
      license='MIT',
      description='Django storage backend to be used with S3',
      py_modules=['cached_s3_storage'])

from boto.utils import parse_ts
from django.core.files.base import File
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage