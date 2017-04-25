from django.contrib.auth.models import *
from rest_framework import viewsets
from API.serializers import *
from API.models import *


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    '''
    Author: group
    Purpose: Sets up view for Customer Class
    '''    
    queryset = Customer.objects.all().order_by('Last_Name')
    serializer_class = CustomerSerializer


class Product_TypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Dara Thomas
    Purpose: Sets up view for Product_Type Class
    '''    
    queryset = Product_Type.objects.all()   
    serializer_class = Product_TypeSerializer


class Payment_TypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Harry Epstein
    Purpose: Sets up view for Payment_Type Class
    '''
    queryset = Payment_Type.objects.all().order_by('Account_Number')
    serializer_class = Payment_TypeSerializer