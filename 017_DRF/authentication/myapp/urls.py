from django.urls import path
from myapp.views import *

urlpatterns = [
    
        path("register",register),
        path("normal",normal_user),
        path("admin1",admin_user),
        path("authenticated",authenticated_user)
]