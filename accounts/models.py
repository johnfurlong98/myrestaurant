# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    CustomUser extends Django's AbstractUser to include additional fields and roles.
    """
    ROLE_CHOICES = [
        ('CUSTOMER', 'Customer'),
        ('ADMIN', 'Administrator'),
    ]
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')
    
    def is_admin(self):
        """
        Check if the user has an administrator role.
        """
        return self.role == 'ADMIN'
    
    def __str__(self):
        return self.username
