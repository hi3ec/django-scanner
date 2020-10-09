from django.db import models
from django.utils import timezone
#from extentions.passive_scanner.sniffer import main
from extentions.passive_scanner.database import readSqliteTable

# Create your models here.
class Devices(models.Model):
    mac_address = models.TextField()
    ip_address = models.TextField()
    os = models.CharField(max_length=200)
    first_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now=True)

    def read_database(self):
        return readSqliteTable()
         