from django.shortcuts import render, redirect
from ingredients.models import Ingredient, UnitOfMeasure
from vendors.models import Vendor
from django.contrib import messages

# Create your views here.

def ingredients(request):
    context = {
        'ingredient_info' : Ingredient.objects.select_related('unit_of_measure', 'vendor')
    }

    print(context)
    
    return render(request, 'ingredients/ingredients.html', context)


def create_ingredient(request):
    if request.method == 'POST':
        Ingredient.objects.create(ingredient_name=request.POST.get('ingredient_name'), ingredient_serving_size=request.POST.get('serving_size'), serving_size_cost= request.POST.get('serving_size_cost'), unit_of_measure= UnitOfMeasure.objects.get(id=request.POST.get('unit_of_measure')), vendor=Vendor.objects.get(id=request.POST.get('ingredient_vendor')))
        messages.success(request, 'Ingredient was created successfully')
        return redirect('ingredients-home')
    else:
        context = {
            'vendors' : Vendor.objects.all(),
            'unit_of_measures' : UnitOfMeasure.objects.all()
        }
        
        return render(request, 'ingredients/create_ingredient.html', context)