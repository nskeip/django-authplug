from copy import copy
from django.contrib.auth import authenticate

class PluggableAuthMiddleware(object):
    def process_request(self, request):
        if 'sign' not in request.REQUEST or 'code' not in request.REQUEST:
            return

        signature = request.REQUEST['sign']
        code = request.REQUEST['code']

        params = copy(request.REQUEST)

        del params['sign']
        del params['code']

        user = authenticate(code=code, params=params, signature=signature)

        return