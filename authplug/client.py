from datetime import datetime
import hashlib

def datetime_ymdh_str(dt):
    return '%s%s%s%s' % (dt.year, dt.month, dt.day, dt.hour,)

def sign(params, salt, date=None):
    items = sorted(params.iteritems())
    hash = u'&'.join([u'='.join((unicode(k), unicode(v))) for k, v in items])
    date = date or datetime_ymdh_str(datetime.utcnow())

    s1 = u''.join((hash, date))
    hash = hashlib.sha1(s1).hexdigest()

    salted_hash = hashlib.sha1(u''.join((hash, salt))).hexdigest()

    return unicode(salted_hash)
