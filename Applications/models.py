from django.db import models
from django.contrib import admin
# Create your models here.
#
#  Application:
#       id
#       name
#       version
#       binary_path
#       info_path
#
class Applicaton(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    binary_path = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name + self.version