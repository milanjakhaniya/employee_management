from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address =models.CharField(max_length=250)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=15)