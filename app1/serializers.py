from .models import Invoice,InvoiceDetail
from rest_framework import serializers


class InvoiceDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = InvoiceDetail
		fields = ['invoice','description','quantity','unit_price','price']


class InvoiceSerializer(serializers.ModelSerializer):
	invoice_details = InvoiceDetailSerializer(many=True,read_only=True)
	class Meta:
		model = Invoice
		fields = ['date','invoice_no','name','invoice_details']
	