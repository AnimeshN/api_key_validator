# api_keys/urls.py
from django.urls import path
from .views import RequestApiKeyView
from .views import TestApiKeyView  # Update this import

urlpatterns = [
    path('request_api_key/', RequestApiKeyView.as_view(), name='request_api_key'),
    path('test/', TestApiKeyView.as_view(), name='test_api_key'),  # Update this line

]
