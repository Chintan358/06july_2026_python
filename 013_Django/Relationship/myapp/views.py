from django.shortcuts import render
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