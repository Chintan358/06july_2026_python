
from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete_product,name="delete"),
    path("retrive",retrive_product,name="retrive"),
    path("update",update_product,name="update")
]