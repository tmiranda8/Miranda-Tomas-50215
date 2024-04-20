from typing import Any
from django.db import models
from datetime import date

class Client(models.Model):
    def __init__(self, *args, **kwargs):
        super(Billing, self).__init__(*args, **kwargs)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    birthday = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)
    phone = models.IntegerField(null=False, blank=True)
    email = models.EmailField(max_length = 64, null=False, blank=True)
    added = models.DateField(auto_now=False, auto_now_add=True)

class CustomerAddress(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length = 64, null=False, blank=False)
    city =  models.CharField(max_length = 32, null=False, blank=False)
    state = models.CharField(max_length = 32, null=False, blank=True)
    zip_code = models.IntegerField(null=False, blank=True)

class Billing(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    corporation = models.BooleanField(default=False)
    CUIT = models.BigIntegerField(null=False, blank=True, default=0)