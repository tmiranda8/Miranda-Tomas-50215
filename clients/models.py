from django.db import models

class UserAccount(models.Model):
    user = models.CharField(max_length=32, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
