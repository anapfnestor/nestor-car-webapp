from django.db import models
from customer.models import Customer
from vehicle.models import Vehicle
from django.utils.timezone import now


class Budget(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    data = models.DateTimeField(default=now)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
