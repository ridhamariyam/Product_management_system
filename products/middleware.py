import re
from django.http import JsonResponse
from django.conf import settings
from .models import User

ALLOWED_IPS = ['127.0.0.1']

class APIKeyAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not re.match(r'^/api/', request.path):
            return self.get_response(request)

        api_key = request.headers.get('API-Key')
        if not api_key or not User.objects.filter(api_key=api_key).exists():
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        return self.get_response(request)

class IPAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ALLOWED_IPS:
            return JsonResponse({'error': 'Forbidden'}, status=403)

        return self.get_response(request)
