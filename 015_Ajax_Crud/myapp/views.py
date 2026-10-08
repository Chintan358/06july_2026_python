from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        brand = data.get("brand")
        
        Product.objects.create(name=name,price=price,qty=qty,brand=brand)
        return HttpResponse("Registration successfully !!!")
    
    
def display(request):
    products = Product.objects.all()
    return JsonResponse({"data":list(products.values())})


def delete_product(request):
    pid = request.GET['pid']
    product = Product.objects.get(id=pid)
    product.delete()
    return HttpResponse("Product deleted")


def retrive_product(request):
    pid = request.GET['pid']
    product = Product.objects.filter(id=pid)
    return JsonResponse({"data":list(product.values())})


def update_product(request):
    if request.method=='POST':
            data = request.POST
            id = data.get("id")
            name = data.get("name")
            price = data.get("price")
            qty = data.get("qty")
            brand = data.get("brand")
            
            product = Product.objects.get(id=id)
            product.name=name
            product.price=price
            product.qty=qty
            product.brand=brand
            product.save()
                        
           
            return HttpResponse("Update successfully !!!")