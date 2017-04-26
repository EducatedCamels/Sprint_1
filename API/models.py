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
    customers = models.ForeignKey(Customer)

class Order(models.Model):
    '''
    Purpose: Expose Order data to Client
    Author: Miriam Rozenbaum
    '''
    created = models.DateField()
    customers = models.ForeignKey(Customer)
    payment_types = models.ForeignKey(PaymentType)


class Product(models.Model):
    '''
    Purpose: Expose Product data to Client
    Author: Bri Wyatt
    '''
    price = models.FloatField()
    title = models.CharField(max_length=255)
    product_types = models.ForeignKey(ProductType)
    description = models.CharField(max_length=255)
    customers = models.ForeignKey(Customer)
    created = models.DateField()


class Computer(models.Model):
    '''
    Purpose: Expose Computer data to Client
    Author: Dean Smith
    '''
    purchase_date = models.DateField()
    decommission_date = models.DateField()
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
    products = models.ForeignKey(Product) 
    orders = models.ForeignKey(Order)
    
class Department(models.Model):
	'''
    Purpose: Expose Department data to Client
    Author: Harry Epstein
    '''
	department_name = models.CharField(max_length=255)
	budget = models.BigIntegerField()




class Employee(models.Model):
    '''
    Purpose: Expose Employee data to Client
    Author: Dara Thomas
    '''
    departments = models.ForeignKey(Department)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    is_supervisor = models.BooleanField( )

class EmployeeComputer(models.Model):
    """
    Author: Dean Smith
    Atributes: EmployeeComputer ID
    """
    employees = models.ForeignKey(Employee)
    computers = models.ForeignKey(Computer)
    start_date = models.DateField()
    end_date = models.DateField()

class EmployeeTrainingProgram(models.Model):
    '''
    Purpose: Expose EmployeeTrainingProgram data to Client
    Author: Dara Thomas
    '''
    training_programs = models.ForeignKey(TrainingProgram)
    employees = models.ForeignKey(Employee)
