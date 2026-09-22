from django.shortcuts import render,redirect
from myapp.models import *
import os

# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def register(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        file = request.FILES.get("file")
        
        if id :
            product = Product.objects.get(id = id)
            product.name = name
            product.price = price
            product.qty = qty
            if file:
                os.remove(product.image.path)
                product.image=file
            product.save()
            msg = "Update successfully"
        else:
            Product.objects.create(name=name,price=price,qty=qty,image=file)
            msg= "Registration successfully !!"
    return render(request,"index.html",{"msg":msg})
    
    
def delete_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id = id)
    if product.image:
        os.remove(product.image.path)
    product.delete()
    return redirect("display")


def update_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id = id)
    return render(request,"index.html",{"product":product})