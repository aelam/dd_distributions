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
    FAMILY_CHOICES = (
        (r'iPad',r'iPad'),
        (r'iPhone',r'iPhone'),
        (r'iPhone,iPad',r'iPhone,iPad'),
        )

    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    binary_path = models.CharField(max_length=200)
    family = models.CharField(max_length=200,choices=FAMILY_CHOICES)

#    new_features = models.TextField()

    def __unicode__(self):
        return self.name + self.version