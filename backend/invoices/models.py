from django.db import models
from clients.models import Client
from companies.models import TransportCompany


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transport_company = models.ForeignKey(TransportCompany, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=10, decimal_places=2)
    sgst = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.client}"

    class Meta:
        ordering = ['-date']


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    date = models.DateField()
    vehicle_number = models.CharField(max_length=20)
    pickup_point = models.CharField(max_length=255)
    delivery_point = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle_number} - {self.pickup_point} to {self.delivery_point}"