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




class Payment_Type(models.Model):
    Account_Number = models.IntegerField()
    #Customer ID is equal to just an instance of the Customer Class
    Customer_ID = models.ForeignKey(Customer)