from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length = 40)
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    password = models.CharField(max_length = 30)