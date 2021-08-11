from django.db import models
from vendors.models import Vendor


# Create your models here.

class UnitOfMeasure(models.Model):
    abbr = models.CharField(max_length=2)
    description = models.CharField(max_length=100)

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=250)
    ingredient_serving_size = models.IntegerField()
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete = models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete= models.CASCADE)
    serving_size_cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)


   