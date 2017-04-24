from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length = 15)
    Last_Name = models.CharField(max_length = 25)
    Created = models.DateField()


class PaymentType(models.Model):
    Account_Number = models.IntegerField()
    #Customer ID is equal to just an instance of the Customer Class
    Customer_ID = models.ForeignKey(Customer)
