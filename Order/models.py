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

    # def __str__(self):
    #     return self.goodsname

    def Buy(self):
        # buy_list = []
        # for c in Customer.objects.filter(Inventory_id_id=self.pk):
        #     buy_list.append(c)
        # return buy_list
        return Customer.objects.filter(Inventory_id=self.pk)

    def Stocks(self):
        return Stock.objects.filter(Inventory_Id=self.pk)
            


class Stock(models.Model):
    Inventory_Id = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    Stock_Name = models.CharField(max_length = 30)

    def __str__(self):
        return self.Stock_Name

class Customer(models.Model):
    Inventory_id = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    Buyer = models.CharField(max_length = 30)
    Status = models.ForeignKey('OrderStatus', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.Buyer

class OrderStatus(models.Model):
    Status_id = models.IntegerField(primary_key=True)
    Status = models.CharField(max_length = 10)

    def __str__(self):
        return self.Status
