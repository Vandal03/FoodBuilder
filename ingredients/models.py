from django.db import models
from vendors.models import Vendor

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=250)
    ingredient_serving_size = models.IntegerField()
    unit_of_measure = models.CharField(max_length=2)
    vendor = models.ForeignKey(Vendor, on_delete= models.PROTECT)
