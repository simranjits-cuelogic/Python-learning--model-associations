from __future__ import unicode_literals

from django.db import models

"""
Note: following models for one to many(1:N) relation.
Company.objects.first().car_set.all()
Company.objects.first().car_set.create(modl = 'nano')
Car.objects.first().manufacturer

"""
class Company(models.Model):
    name = models.CharField(max_length = 10)
    revenue = models.IntegerField(default=0)

    def __str__(self):
        return self.name + "-" + str(self.revenue)

class Car(models.Model):
    manufacturer = models.ForeignKey(Company, on_delete=models.CASCADE)
    # on_delete=models.CASCADE -like-> dependent: destroy

    modl = models.CharField(default='', max_length=15)

    def __str__(self):
        return self.modl
