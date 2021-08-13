from django.urls import path
from . import views as foodlist_views




urlpatterns = [
    path('', foodlist_views.home, name='foodlist-home'),
    path('create/', foodlist_views.create_food_item, name='foodlist-create')
   
]