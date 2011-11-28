from distutils.core import setup

setup(
    name='authplug',
    version='0.1',
    description='Authplug - pluggable auth',
    long_description='An authentication application for django',
    author='nskeip',
    author_email='me@ns-keip.ru',
    url='https://github.com/nskeip/authplug',
    packages=['authplug'],
    requires=['django'],
    license='bsd'
)