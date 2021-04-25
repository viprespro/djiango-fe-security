from django.db import models


# Create your models here.
class Comments(models.Model):
    content = models.CharField(max_length=250)
