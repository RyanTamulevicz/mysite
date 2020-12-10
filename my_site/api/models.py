from django.db import models

# Create your models here.
class Room(models.Model):
    partOneDes = models.CharField(max_length=30, default="")
    partOne = models.CharField(max_length=30, default="")