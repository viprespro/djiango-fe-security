from django.db import models


# Create your models here.
class Comments(models.Model):
    content = models.CharField(max_length=250)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    age = models.IntegerField(0)
