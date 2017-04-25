from django.conf.urls import url, include
from rest_framework import routers
from API import views


router = routers.DefaultRouter()

router.register(r'customer', views.CustomerViewSet)
router.register(r'product_type', views.ProductTypeViewSet)
router.register(r'payment_type', views.PaymentTypeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'productorder', views.ProductOrderViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



