from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("first_name")
        lname = data.get("last_name")
        uname = data.get("username")
        password=data.get("password")
        
        # u = User(first_name=fname,last_name=lname,username=uname)
        # u.set_password(password)
        # u.save()
        
        if User.objects.filter(username=uname).exists():
            return render(request,"reg.html",{"error":"Username already exist !"})

        User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
        
        return render(request,"reg.html",{"message":"Registration successfully !"})
        
        
    return render(request,"reg.html")


def home(request):
    return render(request,"home.html")

def user_logout(request):
    pass
