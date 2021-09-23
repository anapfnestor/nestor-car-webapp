from django.db import models
from customer.models import Customer


class Vehicle(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    model = models.CharField(max_length=255, null=False, blank=False)
    license_plate = models.CharField(max_length=255, null=False, blank=False, unique=True)
    mileage = models.CharField(max_length=255, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

