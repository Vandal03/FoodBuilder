from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import FoodItem, Recipes
from ingredients.models import Ingredient


# Create your views here.
def home(request):
    context = {
       'foods' : FoodItem.objects.all(),
       'recipes' : Recipes.objects.prefetch_related('ingredient_item', 'food_item').all()
    }
    
    return render(request, 'foodlist/home.html', context)


def create_food_item(request):
   return render(request, 'foodlist/create.html')