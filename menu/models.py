from django.db import models

# menu/models.py

from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('APPETIZER', 'Appetizer'),
        ('MAIN', 'Main Course'),
        ('DESSERT', 'Dessert'),
        ('BEVERAGE', 'Beverage'),
    ]

    DIETARY_PREFERENCES = [
        ('NONE', 'None'),
        ('VEGETARIAN', 'Vegetarian'),
        ('VEGAN', 'Vegan'),
        ('GLUTEN_FREE', 'Gluten-Free'),
        ('DAIRY_FREE', 'Dairy-Free'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    dietary_preference = models.CharField(max_length=20, choices=DIETARY_PREFERENCES, default='NONE')
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name

