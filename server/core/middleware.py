import time
from django.utils.deprecation import MiddlewareMixin


class RequestTimingMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = round(time.time() - start, 3)
        print(f"[MIDDLEWARE] {request.path} took {duration}s")
        return response