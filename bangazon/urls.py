from django.conf.urls import url, include
from rest_framework import routers
from API import views


router = routers.DefaultRouter()
#All routs for API resources
router.register(r'customer', views.CustomerViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'paymenttype', views.PaymentTypeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'computer', views.ComputerViewSet)
router.register(r'trainingprogram', views.TrainingProgramViewSet)
router.register(r'productorder', views.ProductOrderViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'employeecomputer', views.EmployeeComputerViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'employeetrainingprogram', views.EmployeeTrainingProgramViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

