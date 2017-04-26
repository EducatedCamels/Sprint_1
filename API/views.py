from django.contrib.auth.models import *
from rest_framework import viewsets
from API.serializers import *
from API.models import *


class CustomerViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
        sorted by Last_Name attribute

    Author: Educated Camels
    Purpose: Queries database for Customer data and sets up view for Customer Class (ordered by last name)
    '''
    queryset = Customer.objects.all().order_by('last_name')
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Author: Bri Wyatt
    Purpose: Queries database for Product data and sets up view for Product(s)
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Dara Thomas
    Purpose: Queries database for Product Type data and sets up view for Product Type
    '''    

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Harry Epstein
    Purpose: Queries database for Payment Type data and sets up view for Payment Type
    '''
    queryset = PaymentType.objects.all().order_by('account_number')
    serializer_class = PaymentTypeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    '''
    Author: Miriam Rozenbaum
    Purpose: Queries database for Order data and sets up view for Order
    '''
    queryset = Order.objects.all().order_by('customer')
    serializer_class = OrderSerializer    


class ComputerViewSet(viewsets.ModelViewSet):
    '''

    API endpoint that allows Computers to be viewed or edited.
        sorted by purchase date attribute

    Author: Dean Smith
    Purpose: Queries database for Computer data and sets up view for Computer Class (ordered by purchase date)
    '''    
    queryset = Computer.objects.all().order_by('purchase_date')
    serializer_class = ComputerSerializer  


class TrainingProgramViewSet(viewsets.ModelViewSet):
    """
    Author: Bri Wyatt 
    Purpose: Queries database for Training Program data and sets up view for TrainingPrograms

    """
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer 


class DepartmentViewSet(viewsets.ModelViewSet):
    '''
    Author: Harry Epstein
    Purpose: Queries database for Department data and sets up view for Departmetn
    Methods: none (yet)
    '''
    queryset = Department.objects.all().order_by('department_name')
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    '''
    Author: Dara Thomas
    Purpose: Queries database for Employee data and sets up view for Employee
    '''
    queryset = Employee.objects.all().order_by('department')
    serializer_class = EmployeeSerializer
