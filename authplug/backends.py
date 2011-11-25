from django.contrib.auth.models import User
from authplug.models import HashKey

class PluggableAuthBackend:
    supports_anonymous_user = False
    supports_object_permissions = False

    def authenticate(self, code, params, signature):
        if not code or not signature:
            return
        try:
            hk = HashKey.objects.get(code=code)
            if hk.signature_ok(params, signature):
                return hk.user
        except HashKey.DoesNotExist:
            return

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None