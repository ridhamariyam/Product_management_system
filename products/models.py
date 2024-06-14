from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('storekeeper', 'Storekeeper'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    api_key = models.CharField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = get_random_string(40)
        super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
