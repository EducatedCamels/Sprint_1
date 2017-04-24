from django.contrib.auth.models import User, Group
from rest_framework import serializers
from API.models import *

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = ('url', 'First_Name', 'Last_Name', 'Created')  


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'Price', 'Title', 'Product_Type_ID', 'Description', 'Customer_ID', 'Date_Created')


