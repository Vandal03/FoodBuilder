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
    if request.method == 'POST':
        Vendor.objects.create(company_name=request.POST.get('company_name'), company_number=request.POST.get('company_number'), rep_name=request.POST.get('rep_name'))
        messages.success(request, 'Vendor was added successfully')
        return redirect('vendors-home')
    else:
        return render(request, 'vendors/create_vendor.html')


def edit_vendor(request, vendor_id):
    if request.method == "POST":
        Vendor.objects.filter(id=vendor_id).update(company_name=request.POST.get('company_name'), company_number=request.POST.get('company_number'), rep_name=request.POST.get('rep_name'))
        return redirect('vendors-home')
    else:
        context ={
            'vendor' : Vendor.objects.filter(id=vendor_id).get()
        }
        return render(request, 'vendors/edit_vendor.html', context)