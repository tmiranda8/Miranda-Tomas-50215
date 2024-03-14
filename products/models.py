from django.db import models
from datetime import date

class Products(models.Model):
    def __str__(self):
        return f'{self.brand} {self.product_model}'
    brand = models.CharField(max_length=32)
    product_model = models.CharField(max_length=32)
    product_type = models.CharField(max_length=32)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    

class NetworkDevice(Products):
    creation = models.DateField(default=date.today)

class IoTDevice(Products):
    creation = models.DateField(default=date.today)
    class Meta:
        verbose_name = "IoT Device"

class HardwareComponent(Products):
    creation = models.DateField(default=date.today)

class GlobalSearch(models.Model):
    name = models.TextField()
    id = models.OneToOneField(Products, on_delete=models.CASCADE, primary_key=True)