import re
from django.shortcuts import render, redirect
from product.models import Product
from product.forms import ProductForm

# Create your views here.

def HomepageView(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/Homepage.html', context)

def AddProductView(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'product/AddProduct.html', context)