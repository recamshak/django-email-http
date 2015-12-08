# coding: utf-8
from setuptools import setup

setup(
    name='django-email-http',
    version='0.1',
    author=u'Joël Billaud',
    author_email='jbillaud@gmail.com',
    packages=['django_email_http'],
    include_package_data=True,
    url='https://github.com/recamshak/django-email-http',
    license='BSD',
    description='Forward emails to a remote server through http. Convenient for E2E testing of user email validation for example.',
    long_description=open('README.rst').read(),
    install_requires=[
        "django >= 1.3",
        "requests >= 2.8"
    ],
)
