from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

class Counters(models.Model):
    name       = models.CharField(default="عدادات الصفحه الرئيسيه" , max_length=50 , editable = False)
    training   = models.CharField(max_length=10)
    youth      = models.CharField(max_length=10)
    followers  = models.CharField(max_length=10)
    events     = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

    