from django.urls import path
from . import views as ingredients_views



urlpatterns = [
    path('', ingredients_views.ingredients, name='ingredients-home')
    
]