# coding: utf-8

from distutils.core import setup

setup(
    name='django-cached-s3-storage',
    version='0.2.1',
    py_modules=['cached_s3_storage'],
    license='MIT',
    author='Ulysses V',
    author_email='uvilela [at] inoa.com.br',
    url='https://github.com/ulyssesv/django-cached-s3-storage',
    description='Django storage backend to be used with S3.',
    long_description=open('README.rst').read()
)
