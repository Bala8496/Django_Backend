from django.db import models

class Vehicle (models.Model):
    name = models.CharField(max_length=255)
    type = models.TextField()
    number = models.CharField(max_length=20)