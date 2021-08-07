from django.shortcuts import render, redirect
from django.http import HttpRequest
from vendors.models import Vendor
from django.contrib import messages

def vendors(request):
    context = {
        'Vendors' : Vendor.objects.all()
    }
    return render(request, 'vendors/vendors.html', context)


def delete_vendor(request, vendor_id):
    Vendor.objects.filter(id=vendor_id).delete()
    messages.success(request, 'Vendor was deleted successfully')
    return redirect('vendors-home')


def create_vendor(request):
    return render(request, 'vendors/create_vendor.html')