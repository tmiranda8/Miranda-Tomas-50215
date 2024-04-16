from django.db import models
from datetime import date

class Products(models.Model):
    class Meta:
        verbose_name = "Product"
    def __str__(self):
        return f'{self.brand} {self.product_model}'
    brand = models.CharField(max_length = 32)
    product_model = models.CharField(max_length = 32)
    product_type = models.CharField(max_length = 32)
    price = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='products', null = True, blank = True)

class NetworkDevice(Products):
    created = models.DateField(default = date.today)

class IoTDevice(Products):
    created = models.DateField(default = date.today)
    class Meta:
        verbose_name = "IoT device"

class HardwareComponent(Products):
    created = models.DateField(default = date.today)

class GlobalSearch(models.Model):
    name = models.TextField()
    id = models.OneToOneField(Products, on_delete = models.CASCADE, primary_key = True)