from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length = 15)  
    Last_Name = models.CharField(max_length = 25)
    Created = models.DateField()

