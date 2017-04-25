from django.db import models


class Customer(models.Model):
	"""
	Purpose: Expose Customer data to Client
	Author: Educated Camels
	"""
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 25)
	created = models.DateField()
    
class ProductType(models.Model):
    """
    Purpose: Expose Product Type data to Client
    Author: Dara Thomas
    """
    category = models.CharField(max_length = 30)

class PaymentType(models.Model):
    """
    Purpose: Expose Payment Type data to Client
    Author: Harry Epstein
    """
    account_number = models.IntegerField()
    customer = models.ForeignKey(Customer)

class Order(models.Model):
    '''
    Purpose: Expose Order data to Client
    Author: Miriam Rozenbaum
    '''
    created = models.DateField()
    customer = models.ForeignKey(Customer) 
    payment_type = models.ForeignKey(PaymentType)   


class Product(models.Model):
    '''
    Purpose: Expose Product data to Client
    Author: Bri Wyatt
    '''
    price = models.FloatField()
    title = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType)
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer)
    created = models.DateField()

class TrainingProgram(models.Model):
    """
    Purpose: Expose Training-Program data to Client
    Author: Bri Wyatt
    
    """
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    class_capacity = models.IntegerField()







