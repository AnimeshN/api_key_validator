# api_keys/middleware.py
from django.http import JsonResponse
from django.urls import resolve
from .models import APIKey

class APIKeyAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Exclude middleware for certain URL paths

        if request.path.startswith('/admin/'):
            return self.get_response(request)

        if resolve(request.path_info).url_name in ['request_api_key']:
            return self.get_response(request)

        # Check for API key in the request headers
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            return JsonResponse({'error': 'API Key is required'}, status=401)

        # if not APIKey.objects.filter(key=api_key, is_active=True).exists():
        #     return JsonResponse({'error': 'Invalid API Key'}, status=403)
        key = APIKey.objects.filter(key=api_key, is_active=True).first()
        if not key or key.is_expired():
            return JsonResponse({'error': 'Invalid or expired API Key'}, status=403)


        return self.get_response(request)
