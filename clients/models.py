from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    phone = models.IntegerField(null=False, blank=True)
    email = models.EmailField(max_length = 64, null=False, blank=True)

class CustomerAddress(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length = 64, null=False, blank=False)
    city =  models.CharField(max_length = 32, null=False, blank=False)
    state = models.CharField(max_length = 32, null=False, blank=True)
    zip_code = models.IntegerField(null=False, blank=True)

class Billing(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    corporation = models.BooleanField()
    CUIT = models.BigIntegerField(null=False, blank=True)