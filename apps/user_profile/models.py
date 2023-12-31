from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from apps.orders.countries import Countries

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    country_region = models.CharField(
        max_length=255, choices=Countries.choices, default=Countries.Colombia)

    def __str__(self):
        return self.user