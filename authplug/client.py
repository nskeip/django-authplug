import datetime
import hashlib

def datetime2str(dt):
    return '%s%s%s%s' % (dt.year, dt.month, dt.day, dt.hour,)

def sign(params, salt, date=None):
    items = sorted(params.iteritems())
    hash = u'&'.join([u'='.join((unicode(k), unicode(v))) for k, v in items])
    date = date or datetime2str(datetime.utcnow())

    #прибаляем дату в формате UTC2 и применяем sha1
    s1 = u''.join((hash, date))
    hash = hashlib.sha1(s1).hexdigest()
    #добавляем ключ и применяем sha1
    hash = hashlib.sha1(u''.join((hash, salt))).hexdigest()

    return unicode(hash)