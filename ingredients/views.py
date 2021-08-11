from django.shortcuts import render, redirect
from ingredients.models import Ingredient, UnitOfMeasure
from vendors.models import Vendor
from django.contrib import messages

# Create your views here.

def ingredients(request):
    context = {
        'ingredient_info' : Ingredient.objects.select_related('unit_of_measure', 'vendor'),
        
    }
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


def delete_ingredient(request, ingredient_id):
    Ingredient.objects.filter(id=ingredient_id).delete()
    messages.success(request, "Ingredient was deleted successfully")
    return redirect('ingredients-home')


def edit_ingredient(request, ingredient_id):
    if request.method == 'POST':
        Ingredient.objects.filter(id = ingredient_id).update(ingredient_name=request.POST.get('ingredient_name'), ingredient_serving_size=request.POST.get('serving_size'), serving_size_cost= request.POST.get('serving_size_cost'), unit_of_measure= UnitOfMeasure.objects.get(id=request.POST.get('unit_of_measure')), vendor=Vendor.objects.get(id=request.POST.get('ingredient_vendor')))
        return redirect('ingredients-home')
    else:
        
        context = {
            'vendors' : Vendor.objects.all(),
            'unit_of_measures' : UnitOfMeasure.objects.all(),
            'ingredient_info' : Ingredient.objects.filter(id = ingredient_id).select_related('unit_of_measure', 'vendor').get()
        }
        # print(context)
        return render(request, 'ingredients/edit_ingredient.html', context)
    