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
    created = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer)
    payment_type = models.ForeignKey(PaymentType)


class Product(models.Model):
    '''
    Purpose: Expose Product data to Client
    Author: Bri Wyatt
    '''
    price = models.FloatField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateField()
    product_type = models.ForeignKey(ProductType)
    customer = models.ForeignKey(Customer)


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
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
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
    '''
	department_name = models.CharField(max_length=255)
	budget = models.BigIntegerField()




class Employee(models.Model):
    '''
    Purpose: Expose Employee data to Client
    Author: Dara Thomas
    '''
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    is_supervisor = models.BooleanField()
    department = models.ForeignKey(Department)

class EmployeeComputer(models.Model):
    """
    Author: Dean Smith
    Atributes: EmployeeComputer ID
    """
    start_date = models.DateField()
    end_date = models.DateField()
    employee = models.ForeignKey(Employee)
    computer = models.ForeignKey(Computer)

class EmployeeTrainingProgram(models.Model):
    '''
    Purpose: Expose EmployeeTrainingProgram data to Client
    Author: Dara Thomas
    '''
    training_program = models.ForeignKey(TrainingProgram)
    employee = models.ForeignKey(Employee)
