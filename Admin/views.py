from django.shortcuts import render,redirect
from . import models

def home(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    context = {
        'products': products,
        'categories': categories
        }
    return render(request,'index.html',context)

def about(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request,'about.html',context)

def contact(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request,'contact.html',context)

def categories(request):
    categories = models.Category.objects.all()[:15]
    products = models.Product.objects.all()
    context = {
        'products': products,
        'categories': categories
        }
    return render(request,'categories.html',context)

def specific_category(request,slug):
    categories = models.Category.objects.all()
    products = models.Product.objects.filter(category__slug=slug)
    context = {
        'products': products,
        'categories': categories
        }
    return render(request,'categories.html',context)

def product(request,code):
    try:
        product = models.Product.objects.get(product_code=code)
    except:
        return redirect('/')
    categories = models.Category.objects.all()
    context = {
        'product': product,
        'categories': categories
        }
    return render(request,'single.html',context)

# def home5(request):
#     categories = models.Category.objects.all()
#     context = {
#         'categories': categories
#         }
#     return render(request,'products.html',context)
