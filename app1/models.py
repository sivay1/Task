from django.db import models

# Create your models here.

class Invoice(models.Model):
	date = models.DateField()
	invoice_no = models.CharField(max_length=50)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.invoice_no
class InvoiceDetail(models.Model):

	invoice = models.ForeignKey(Invoice,related_name = 'invoice_details',on_delete = models.CASCADE)
	description = models.CharField(max_length = 255)
	quantity = models.SmallIntegerField()
	unit_price = models.DecimalField(max_digits = 6 , decimal_places = 2) 
	price = models.DecimalField(max_digits = 6 , decimal_places = 2)

	def __str__(self):
		return self.description


