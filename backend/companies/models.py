from django.db import models


class TransportCompany(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=20)
    sac_number = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Transport Company"
        verbose_name_plural = "Transport Companies"