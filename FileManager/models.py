from django.db import models

# Create your models here.
#encoding=utf-8

from django.db import models

class Photo(models.Model):
    file = models.FileField(upload_to='photos/%Y/%m/%d',blank=True,null=True)




