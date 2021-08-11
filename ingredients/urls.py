from django.urls import path
from . import views as ingredients_views



urlpatterns = [
    path('', ingredients_views.ingredients, name='ingredients-home'),
    path('create/', ingredients_views.create_ingredient, name='ingredient-create'),
    path('<int:ingredient_id>/delete', ingredients_views.delete_ingredient, name='ingredient-delete'),
    path('<int:ingredient_id>/edit', ingredients_views.edit_ingredient, name='ingredient-edit')
]