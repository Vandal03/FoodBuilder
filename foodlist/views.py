from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import FoodItem, Quantities
from ingredients.models import Ingredient

# Create your views here.
def home(request):
    
    context = {
        'food_items' : FoodItem.objects.all().prefetch_related('ingredients')
        
    }
    return render(request, 'foodlist/home.html', context)