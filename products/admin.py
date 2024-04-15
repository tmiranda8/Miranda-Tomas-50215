from django.contrib import admin
from products import models

admin.site.register(models.Products)
admin.site.register(models.GlobalSearch)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IoTDevice)
admin.site.register(models.HardwareComponent)