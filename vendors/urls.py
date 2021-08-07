from django.contrib import admin
from django.urls import path
from . import views as vendor_views


urlpatterns = [
    path('', vendor_views.vendors, name='vendors-home'),
    path('<int:vendor_id>/delete', vendor_views.delete_vendor, name='vendor-delete'),
    path('create/', vendor_views.create_vendor, name='vendor-create'),
    path('<int:vendor_id>/edit', vendor_views.edit_vendor, name='vendor-edit')
    
]