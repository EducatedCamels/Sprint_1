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

class ProductOrder(models.Model):
    '''
    Purpose: Expose Product Order data to Client
    Author: Miriam Rozenbaum
    '''
    product = models.ForeignKey(Product) 
    order = models.ForeignKey(Order)
    
class Department(models.Model):
	'''
    Purpose: Expose Department data to Client
    Author: Harry Epstein
    Method: none (yet)
    '''
	department_name = models.CharField(max_length=255)
	budget = models.BigIntegerField()

