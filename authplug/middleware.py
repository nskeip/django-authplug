from django.contrib.auth import authenticate

class PluggableAuthMiddleware(object):
    def process_request(self, request):
        if 'sign' not in request.REQUEST or 'code' not in request.REQUEST:
            return

        signature = request.REQUEST['sign']
        code = request.REQUEST['code']

        params = dict(request.REQUEST) # to copy, not have a link

        del params['sign']
        del params['code']

        user = authenticate(code=code, params=params, signature=signature)
        if user:
            request.user = user