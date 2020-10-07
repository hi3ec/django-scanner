from django.db import models
from django.utils import timezone

# Create your models here.
class Device_Found(models.Model):
    mac_address = models.TextField()
    ip_address = models.TextField()
    os = models.CharField(max_length=200)
    first_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now=True)