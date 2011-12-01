from distutils.core import setup

setup(
    name='django-authplug',
    version='0.1.3',
    description='Authplug - pluggable auth',
    long_description='An authentication application for django',
    author='nskeip',
    author_email='me@ns-keip.ru',
    url='https://github.com/mediasite/authplug',
    packages=['authplug'],
    requires=['django'],
    license='bsd'
)
