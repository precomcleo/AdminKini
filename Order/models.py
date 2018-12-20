from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Inventory(models.Model):  
    Purchase_Date = models.DateField()
    Type = models.CharField(max_length=5, null=True,blank=True)
    Weight = models.FloatField(null=True,blank=True)
    Estimated_Weight = models.FloatField(null=True,blank=True)
    shipment_Num = models.CharField(max_length=15, null=True,blank=True)
    goodsname = models.CharField(max_length=15)
    specification = models.CharField(max_length=15, null=True,blank=True)
    Buyer1 = models.CharField(max_length=15, null=True,blank=True)
    Buyer2 = models.CharField(max_length=15, null=True,blank=True)
    Buyer3 = models.CharField(max_length=15, null=True,blank=True)
    Buyer4 = models.CharField(max_length=15, null=True,blank=True)
    Buyer5 = models.CharField(max_length=15, null=True,blank=True)
    Stock1 = models.CharField(max_length=15, null=True,blank=True)
    Stock2 = models.CharField(max_length=15, null=True,blank=True)
    Stock3 = models.CharField(max_length=15, null=True,blank=True)
    Stock4 = models.CharField(max_length=15, null=True,blank=True)
    Stock5 = models.CharField(max_length=15, null=True,blank=True)

    def __str__(self):
        return self.goodsname