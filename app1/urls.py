
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet,InvoiceDetailView
from . import views

router = DefaultRouter()
router.register(r'invoices',InvoiceViewSet)

urlpatterns = [

        
        path('',include(router.urls)),
        path("invoice-details/",views.InvoiceDetailView.as_view()),
        
        
]
