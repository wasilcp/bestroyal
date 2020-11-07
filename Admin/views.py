from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    return render(request,'index.html',{})

def home2(request):
    return render(request,'about.html',{})

def home3(request):
    return render(request,'contact.html',{})

def categories(request):
    categories = models.Category.objects.all()
    return render(request,'categories.html',{'categories': categories})

def home5(request):
    return render(request,'products.html',{})

def home6(request):
    return render(request,'single.html',{})
