from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    salary = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=15)

    def __str__(self):
        return self.name   

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField(max_length=1,validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.testimonial