from django.db import models
from datetime import date

class NetworkDevices(models.Model):
    def __str__(self):
        return 'Dispositivos de Red'
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32, primary_key=True)
    product_type = models.CharField(max_length=32)
    release_date = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)

class IoTDevices(models.Model):
    def __str__(self):
        return 'Dispositivos Smart'
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32, primary_key=True)
    product_type = models.CharField(max_length=32)
    release_date = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)

class ServerHardwareComponents(models.Model):
    def __str__(self):
        return 'Componentes del servidor'
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32, primary_key=True)
    product_type = models.CharField(max_length=32)
    release_date = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)
