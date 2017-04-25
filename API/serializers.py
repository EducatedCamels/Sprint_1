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
        fields = ('url', 'price', 'title', 'product_type', 'description', 'customer', 'created')


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
        fields = ('url', 'account_number', 'customer')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Order data (from queryset on views.py) and serializes into json format
    Author: Miriam Rozenbaum
    """
    class Meta:
        model = Order
        fields = ('url', 'payment_type', 'customer', 'created')

        
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
        fields = ('url', 'product', 'order')

        
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Department data (from queryset on views.py) and serializes into json format
    Author: Harry Epstein
    Method: none (yet)
    """

    class Meta:
        model = Department
        fields = ('url', 'department_name', 'budget')


