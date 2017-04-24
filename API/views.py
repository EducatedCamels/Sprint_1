
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
    API endpoint that allows groups to be viewed or edited.
        sorted by Last_Name attribute
    '''    
    queryset = Customer.objects.all().order_by('Last_Name')
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    API endpoint exposing data in Products
    '''
    queryset = ProductViewSet.objects.all()
    serializer_class = ProductSerializer

