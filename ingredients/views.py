from django.shortcuts import render
from ingredients.models import Ingredient

# Create your views here.

def ingredients(request):
    context = {
        'Ingredients' : Ingredient.objects.all()
    }
    return render(request, 'ingredients/ingredients.html', context)