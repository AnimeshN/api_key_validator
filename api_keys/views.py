# api_keys/views.py
from django.utils.timezone import now
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APIKey
from .decorators import require_api_key
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class RequestApiKeyView(APIView):
    def get(self, request, *args, **kwargs):
        # Check for the most recent key
        latest_key = APIKey.objects.filter(is_active=True).order_by('-created_at').first()
        if latest_key and (now() - latest_key.created_at) < settings.API_KEY_EXPIRATION:
            # Return the most recent key if it was created less than an hour ago
            return Response({'api_key': latest_key.key}, status=status.HTTP_200_OK)
        else:
            # Otherwise, generate a new key
            new_key = APIKey.objects.create()
            return Response({'api_key': new_key.key}, status=status.HTTP_201_CREATED)

# @require_api_key
# def test_api_key(request):
#     return JsonResponse({'message': 'You have accessed a protected resource with a valid API key!'}, status=200)


@method_decorator(require_api_key, name='dispatch')
class TestApiKeyView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'success!'}, status=200)

