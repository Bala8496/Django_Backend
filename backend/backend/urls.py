from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet
from companies.views import TransportCompanyViewSet
from invoices.views import InvoiceViewSet, InvoiceItemViewSet
from vehicles.views import VehicleViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'transport-companies', TransportCompanyViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-items', InvoiceItemViewSet)
router.register(r'vehicle' , VehicleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]