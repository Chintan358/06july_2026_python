from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *


def index(request):
    form = EmployeeForm()
    if request.method=='POST':
        data = EmployeeForm(data=request.POST)
        if data.is_valid():
            data.save()
            return render(request,"index.html",{"form":form,"msg":"Registration successfully"})
        else:
            return render(request,"index.html",{"form":form,"msg":"something went wrong"})
        
    return render(request,"index.html",{"form":form})


def display(request):
    emps = Employee.objects.all()
    return render(request,"display.html",{"emps":emps})

def delete_emp(request):
    id = request.GET.get("id")
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("display")


def update_emp(request):
    id = request.GET.get("id")
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp)
    
    if request.method=='POST':
            data = EmployeeForm(request.POST,       
                                mp)
            if data.is_valid():
                data.save()
                return render(request,"index.html",{"form":form,"msg":"Registration successfully"})
            else:
                return render(request,"index.html",{"form":form,"msg":"something went wrong"})
    
    
    return render(request,"index.html",{"form":form})