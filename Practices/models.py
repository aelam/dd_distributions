from django.db import models

# Create your models here.
class Practice(models.Model):
    title = models.TextField(max_length=100),
    content = models.CharField(max_length=1000)
