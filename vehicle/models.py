from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    model = models.CharField(max_length=255, null=False, blank=False)
    license_plate = models.CharField(max_length=255, null=False, blank=False, unique=True)
    mileage = models.CharField(max_length=255, null=False, blank=False)