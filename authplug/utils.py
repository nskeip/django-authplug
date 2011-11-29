from functools import wraps
from django.http import HttpResponse
from django.utils.decorators import available_attrs

def user_passes_test_403(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return HttpResponse(status=403)
        return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)
    return decorator


def login_required_or_403(function=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test_403(lambda u: u.is_authenticated())
    if function:
        return actual_decorator(function)
    return actual_decorator
