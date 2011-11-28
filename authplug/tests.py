from copy import deepcopy
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.utils import unittest
from authplug.middleware import PluggableAuthMiddleware
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

    def test_good_man_test_middleware(self):
        signature = sign(self.params, self.salt)
        self.params['code'] = self.code
        self.params['sign'] = signature

        params_copy = deepcopy(self.params)

        # middleware testing...
        fake_view = lambda request: getattr(request, 'user', None)
        rf = RequestFactory()
        request = rf.get('/some/private/view/', data=self.params)

        plug_mw = PluggableAuthMiddleware()
        plug_mw.process_request(request=request)

        user_as_response = fake_view(request)

        self.assertFalse(user_as_response is None, msg='fake_view returned None instead of good_user')

        self.assertEqual(user_as_response, self.good_user, msg='wrong user returned')

        # params were not hurt...
        self.assertEqual(params_copy, self.params, msg='params were likely hurt in the middleware')