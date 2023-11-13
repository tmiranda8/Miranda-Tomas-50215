from django.contrib import admin
# Register your models here.
from sites import models

admin.site.register(models.GlobalSearch)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IoTDevice)
admin.site.register(models.HardwareComponent)