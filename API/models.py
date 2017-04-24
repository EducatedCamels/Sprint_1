from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length = 15)  
    Last_Name = models.CharField(max_length = 25)
    Created = models.DateField()

    def __str__(self):
        return self.First_Name + self.Last_Name

class Product(models.Model):
    """by-briwyatt

    Attributes:
        Customer_ID         : expose Customer_ID
        Date_Created        : expose the date the product was created
        Description         : Specs and Summary of a product 
        Price               : a number to expose the price of a product
        Price_Type_ID       : category of product ("home goods")
        Title               : the name of the product
    """
    Price = models.FloatField()
    Title = models.CharField(max_length=255)
    Product_Type_ID = models.ForeignKey(Product_Type_ID)
    Description = models.CharField(max_length=255)
    Customer_ID = models.ForeignKey(Customer, related_name='customer')
    Created = models.DateField()

