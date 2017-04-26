from django.contrib.auth.models import User, Group
from rest_framework import serializers
from API.models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Customer data (from queryset on views.py) and serializes into json format
    Author: Educated Camels
    """
    class Meta:
        model = Customer
        fields = ('url', 'first_name', 'last_name', 'created')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Product data (from queryset on views.py) and serializes into json format
    Author: Bri Wyatt
    """
    class Meta:
        model = Product
        fields = ('url', 'price', 'title', 'product_types', 'description', 'customers', 'created')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Product Type data (from queryset on views.py) and serializes into json format
    Author: Dara Thomas
    """
    class Meta:
        model = ProductType
        exclude = ()


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Payment Type data (from queryset on views.py) and serializes into json format
    Author: Harry Epstein
    """
    class Meta:
        model = PaymentType
        fields = ('url', 'account_number', 'customers')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Order data (from queryset on views.py) and serializes into json format
    Author: Miriam Rozenbaum
    """
    class Meta:
        model = Order
        fields = ('url', 'payment_types', 'customers', 'created')


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Computers data (from queryset on views.py) and serializes into json format
    Author: Dean Smith
    """
    class Meta:
        model = Computer
        fields = ('url', 'purchase_date', 'decommission_date', 'computer_type')  

        
class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Training Program Type data (from queryset on views.py) and serializes into json format
    Author: Bri Wyatt
    """
    class Meta:
        model = TrainingProgram
        fields = ('url', 'title', 'start_date', 'end_date', 'class_capacity')



class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Product Order data (from queryset on views.py) and serializes into json format
    Author: Miriam Rozenbaum
    """
    class Meta:
        model = ProductOrder
        fields = ('url', 'products', 'orders')

        
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Department data (from queryset on views.py) and serializes into json format
    Author: Harry Epstein
    Method: none (yet)
    """

    class Meta:
        model = Department
        fields = ('url', 'department_name', 'budget')

class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    docstring for EmployeeComputerSerializer
    Purpose: Takes database query for Customer data (from queryset on views.py) and serializes into json format
    Author: Dean Smith
    """
    class Meta:
        model = EmployeeComputer
        fields = ('url', 'employees', 'computers', 'start_date', 'end_date')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Employee data (from queryset on views.py) and serializes into json format
    Author: Dara Thomas
    """

    class Meta:
        model = Employee
        fields = ('url', 'departments', 'first_name', 'last_name', 'is_supervisor' )


class EmployeeTrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for EmployeeTrainingProgram data (from queryset on views.py) and serializes into json format
    Author: Dara Thomas
    """
    class Meta:
        model = EmployeeTrainingProgram
        fields = ('url', 'training_programs', 'employees')
