from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    cnpj_document = models.CharField(max_length=20, null=False, blank=False)
    rg_document = models.CharField(max_length=20, null=True, blank=True)
    ie_number = models.CharField(max_length=20, null=True, blank=True)
    im_document = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=400, null=False, blank=False)
    main_phone = PhoneNumberField(null=False, blank=False, unique=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
