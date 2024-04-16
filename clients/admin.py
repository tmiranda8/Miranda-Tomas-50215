from django.contrib import admin
from clients import models

admin.site.register(models.Client)
admin.site.register(models.Billing)
admin.site.register(models.CustomerAddress)