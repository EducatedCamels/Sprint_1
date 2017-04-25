from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length = 15)  
    Last_Name = models.CharField(max_length = 25)
    Created = models.DateField()

    def __str__(self):
        return self.First_Name + self.Last_Name

class Product(models.Model):
    '''author: Bri Wyatt
    
       This Class will act as API endpoint for Products

    Attributes:
        customer_ID         : Customer ID
        date_Created        : the date the product was created
        description         : product specs and summary of a product 
        price               : a number to expose the price of a product
        product_Type        : product type id 
        title               : the name of the product
    '''
    price = models.FloatField()
    title = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, related_name='product')
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, related_name='customer')
    created = models.DateField()
