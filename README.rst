===============================================
Authplug - pluggable django authentication tool
===============================================

-----------
Description
-----------

A django application (actualy, a middleware and a backend) that allows us:

* to sign our requests and to be authenticated with the signature and some other thing ;)
* not to be responsible for storing the state on client

Requirements
------------

* django (developed under 1.3.1 - it is likely that older versions will be okay)

Installation on server
----------------------

1. ``pip install -e git+http://github.com/nskeip/authplug/#egg=authplug``

2. Put ``authplug.middleware.PluggableAuthMiddleware`` to your ``MIDDLEWARE_CLASSES``.

3. Disable ``django.middleware.csrf.CsrfViewMiddleware``.
    Your ``MIDDLEWARE_CLASSES`` might look like this:
    ::

        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            #'django.middleware.csrf.CsrfViewMiddleware',
            'authplug.middleware.PluggableAuthMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        )

4. Put ``authplug.backends.PluggableAuthBackend`` to your ``AUTHENTICATION_BACKENDS``.

   If there is no ``AUTHENTICATION_BACKENDS`` variable in your ``settings.py``,
   you can create it (maybe you will need to add ``django.contrib.auth.backends.ModelBackend``).
   Your ``AUTHENTICATION_BACKENDS`` might look like this:
   ::

        AUTHENTICATION_BACKENDS = (
            'authplug.backends.PluggableAuthBackend',
            'django.contrib.auth.backends.ModelBackend',)

Installation on client
----------------------

Simply run:
    ``pip install -e git+http://github.com/nskeip/authplug/#egg=authplug``

Now you can try to ``import authplug`` in python console.

Signing json-requests in your code.
::

    import urllib
    import urllib2
    from django.conf import settings
    from authplug.client import sign

    data = {
        'param1': 'value1',
        'param2': 'value2',
        # ...
        'paramN': 'valueN',
    }

    signature = sign(data, settings.MY_SECRET_KEY)
    data['code'] = settings.MY_SECRET_ID
    data['sign'] = signature

    try:
        u = urllib2.urlopen('http://example.com/some_service_uri/', data=urllib.urlencode(data))
        result = json.loads(u.read())
    except Exception as e:
        print 'Fail', e
    else:
        print 'Result:', result

