from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    gst_number = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"