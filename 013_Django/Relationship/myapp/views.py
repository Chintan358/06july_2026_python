from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        mfg_date = data.get("mfg_date")
        brand  =data.get("brand")
        category = Category.objects.get(id=data.get("category"))
        
        Product.objects.create(name=name,price=price,qty=qty,mfg = mfg_date,brand=brand,category=category)
        
        
            
    categoris = Category.objects.all()
    return render(request,"index.html",{"categoris":categoris})


def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})


def delete_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")


def update_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    categoris = Category.objects.all()
    
    
    if request.method=='POST':
            data = request.POST
            product.name = data.get("name")
            product.price = data.get("price")
            product.qty = data.get("qty")
            product.mfg_date = data.get("mfg_date")
            product.brand  =data.get("brand")
            product.category = Category.objects.get(id=data.get("category"))
            
            product.save()
            
            return render(request,"index.html")
        
    return render(request,"index.html",{"product":product,"categoris":categoris})