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


class Computer(models.Model):
    '''author: Dean Smith
    
       This Class will act as API endpoint for Products

        Attributes           : Computer ID
        purchase_date        : The date when the company purchased the computer
        decommission_date    : the date when computer is decommissioned by the company
        computer_type        : Brand of company computer
    '''
    
    purchase_date = models.DateField()
    decommision_date = models.DateField()
    computer_type = models.CharField(max_length=20)

class TrainingProgram(models.Model):
    """
    Purpose: Expose Training-Program data to Client
    Author: Bri Wyatt
    
    """
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    class_capacity = models.IntegerField()


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


class Employee(models.Model):
    '''
    Purpose: Expose Employee data to Client
    Author: Dara Thomas
    '''
    department = models.ForeignKey(Department, related_name='department')
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    is_supervisor = models.BooleanField( )


class EmployeeTrainingProgram(models.Model):
    '''
    Purpose: Expose EmployeeTrainingProgram data to Client
    Author: Dara Thomas
    '''
    training_program = models.ForeignKey(TrainingProgram, related_name='training_program')
    employee = models.ForeignKey(Employee, related_name='employee')


