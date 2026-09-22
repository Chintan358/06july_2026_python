from django.urls import path
from myapp.views import *

urlpatterns =[
    path("",user_login,name="login"),
    path("register",register,name="register"),
    path("home",home, name="home"),
    path("logout",user_logout,name="logout")
    
]