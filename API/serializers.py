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

class Product_TypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product_Type
        exclude = ()  