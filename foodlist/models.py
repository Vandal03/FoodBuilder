from django.db import models
from ingredients.models import Ingredient


# Create your models here.
class FoodItem(models.Model):
    food_item_name = models.CharField(max_length=100)
    sell_at = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    cost = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    upc = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, through='Recipes')

    

class Recipes(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    ingredient_item = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    serving_quantity = models.IntegerField()
    
    
   
 