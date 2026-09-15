from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    data = request.POST
    id = data.get("id")
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    
    if id:
        st = Student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.age = age
        st.save()
        return render(request,"index.html",{"msg":"Update success"})
        
    else:
        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg":"Registration success"})

def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})

def delete_student(request):
    id = request.GET.get("id")
    st = Student.objects.get(id=id)
    st.delete()
    return redirect("display")

def update_student(request):
    id = request.GET.get("id")
    st = Student.objects.get(id=id)
    return render(request,"index.html",{"st":st})