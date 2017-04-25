from django.db import models

# Create your models here.
class Customer(models.Model):
	"""
	Purpose: Expose Customer data to Client
	Author: Educated Camels
	Method: none (yet)
	"""
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 25)
	created = models.DateField()

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


class ProductType(models.Model):
    """
    Purpose: Expose Product Type data to Client
    Author: Dara Thomas
    Method: none (yet)
    """
    category = models.CharField(max_length = 30)

<<<<<<< HEAD

=======
>>>>>>> 3c2ee9f4890c39418b3df0e568da000f2f868df4
class PaymentType(models.Model):

    """
    Purpose: Expose Payment Type data to Client
    Author: Harry Epstein
    Method: none (yet)
    """
    account_number = models.IntegerField()
    #Customer ID is equal to just an instance of the Customer Class
    customer = models.ForeignKey(Customer)

class Order(models.Model):
    created = models.DateField()
    customer = models.ForeignKey(Customer) 
    payment_type = models.ForeignKey(PaymentType)   

