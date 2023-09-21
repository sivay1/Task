from django.shortcuts import render
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer

from rest_framework import generics,viewsets

class InvoiceDetailView(generics.ListCreateAPIView):
	queryset = InvoiceDetail.objects.all()
	serializer_class = InvoiceDetailSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer

