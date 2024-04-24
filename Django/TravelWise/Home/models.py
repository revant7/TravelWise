from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=52)
    branch = models.CharField(max_length=26)
    password = models.CharField(max_length=52)
