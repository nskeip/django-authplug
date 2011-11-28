from django.contrib.auth.models import User
from django.utils import unittest
from client import sign
from authplug.models import HashKey

class AuthPlugTestCase(unittest.TestCase):
    def setUp(self):
        self.good_user = User.objects.create_user('John', 'john_smith@example.com', 'password')
        self.bad_user = User.objects.create_user('313373 H4Xor', 'killer@mail.ru',  '12345')

        self.code = 'GOOD'
        self.salt = 'SALT'
        self.hk = HashKey.objects.create(user=self.good_user, code=self.code, salt=self.salt)
        self.params = {'param1' : 'value1', 'param2': 'value2'}

    def tearDown(self):
        User.objects.all().delete()
        HashKey.objects.all().delete()

    def test_good_man_params_signature_ok(self):
        signature = sign(self.params, self.salt)
        self.assertTrue(self.hk.signature_ok(self.params, signature))
