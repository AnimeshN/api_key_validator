from django.db import models
import uuid
from django.utils.timezone import now
from django.conf import settings


def default_expires_at():
    return now() + settings.API_KEY_EXPIRATION

class APIKey(models.Model):
    key = models.CharField(max_length=40, primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # expires_at = models.DateTimeField(default=lambda: now() + timedelta(seconds=30))
    expires_at = models.DateTimeField(default=default_expires_at)  # Use the function here


    def __str__(self):
        return f"{self.key} ({'active' if self.is_active else 'inactive'})"

    def is_expired(self):
        return now() > self.expires_at
