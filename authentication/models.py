from django.db import models
from products.models import User
import secrets

class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, default=secrets.token_urlsafe)

    def __str__(self):
        return self.key

    def is_valid(self):
        return True
