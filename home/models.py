from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import GenericIPAddressField as IPAddressField
from django.contrib.auth.models import User
from django.utils import timezone



class Servers(models.Model):

    class types(models.TextChoices):
        cucm = 'CUCM'
        cuc = 'CUC'
        ucs = 'UCS'
        uccx = 'UCCX'
    server_type = models.CharField(max_length=100,choices=types.choices)
    hostname = models.CharField(unique=True, max_length=20, default=None)
    ipaddress = models.GenericIPAddressField(primary_key=True,default=None)
    fqdn = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fqdn