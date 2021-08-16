from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import FoodItem, Recipes
from ingredients.models import Ingredient, UnitOfMeasure
import random
import time


# Create your views here.
def home(request):
    context = {
       'foods' : FoodItem.objects.all(),
       'recipes' : Recipes.objects.prefetch_related('ingredient_item', 'food_item').all()
    }
    
    return render(request, 'foodlist/home.html', context)


def create_food_item(request):

   #Look into ensuring upc doesn't exist in table
   random.seed(int(time.time()))
   upc = random.randint(123456000000, 123456999999)

   context = {
      'ingredients' : Ingredient.objects.select_related('unit_of_measure').order_by('ingredient_name'),
      'upc' : upc
   }

   

   return render(request, 'foodlist/create_fooditem.html', context)