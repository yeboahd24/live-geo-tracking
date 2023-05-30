# tracker/models.py

from django.db import models

class UserLocation(models.Model):
    ip_address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)