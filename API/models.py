from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length = 15)  
    Last_Name = models.CharField(max_length = 25)
    Created = models.DateField()

class Product_Type(models.Model):
	"""
	Purpose: Expose Product_Type data to Client
	Author: Dara Thomas
	Method: none (yet)
	"""
	Category = models.CharField(max_length = 30)