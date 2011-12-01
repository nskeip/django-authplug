# -*- coding: UTF-8 -*-
import string
import random
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
import client


def create_randstring_maker(count):
    def _make_randstring():
        a =  string.ascii_letters + string.digits
        return ''.join([random.choice(a) for _ in xrange(count)])
    
    return _make_randstring


class HashKey(models.Model):
    user = models.OneToOneField(User)
    code = models.SlugField(unique=True)
    salt = models.CharField(max_length=20, unique=True, default=create_randstring_maker(20))

    @staticmethod
    def sign(params, salt, date=None):
        return client.sign(params, salt, date)

    @staticmethod
    def signs_range(params, salt):
        utc_dates = [client.datetime_ymdh_str(datetime.utcnow() + timedelta(hours=a)) for a in xrange(-1, 2)]
        return [HashKey.sign(params, salt, dt) for dt in utc_dates]

    def signature_ok(self, params, signature):
        return signature in self.signs_range(params, self.salt)

    def __unicode__(self):
        return u'%s (partner)' % self.code
