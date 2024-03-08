import time
from functools import wraps

from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _


def limit_rate(num_requests, period):
    def decorator(view_func):
        request_history = []

        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            current_time = time.time()

            request_history[:] = [timestamp for timestamp in request_history if timestamp > current_time - period]

            if len(request_history) >= num_requests:
                response_len_ratelimit = {
                    "message": _("Превышен лимит"),
                }
                return Response(response_len_ratelimit, status=status.HTTP_429_TOO_MANY_REQUESTS)

            request_history.append(current_time)
            return view_func(*args, **kwargs)

        return wrapped_view

    return decorator
