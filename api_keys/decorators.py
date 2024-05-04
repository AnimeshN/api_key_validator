# api_keys/decorators.py
from django.utils.decorators import decorator_from_middleware
from .middleware import APIKeyAuthenticationMiddleware

require_api_key = decorator_from_middleware(APIKeyAuthenticationMiddleware)
