from django.db import models

# Create your models here.
class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=([('N','Nacional'),('I','Internacional')]),default='N')
    price = models.PositiveIntegerField()