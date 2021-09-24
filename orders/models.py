from django.db import models
from customer.models import Customer
from vehicle.models import Vehicle
from django.utils.timezone import now


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    data = models.DateTimeField(default=now)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=510, null=False, blank=False)
    price = models.DecimalField(null=False, blank=False)
    discount = models.DecimalField(default=0, null=False, blank=False)
    total_price = models.DecimalField(null=False, blank=False)

    def __str__(self):
        return self.name

