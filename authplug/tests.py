from django.contrib.auth.models import User
from django.utils import unittest
from authplug.models import HashKey

class AuthPlugTestCase(unittest.TestCase):
    def setUp(self):
        self.good_user = User.objects.create_user('John', 'john_smith@example.com', 'password')
        self.bad_user = User.objects.create_user('313373 H4Xor', 'killer@mail.ru',  '12345')

        self.hk = HashKey.objects.create(user=self.good_user, code='GOOD', salt='SALT')

    def tearDown(self):
        User.objects.all().delete()
        HashKey.objects.all().delete()


