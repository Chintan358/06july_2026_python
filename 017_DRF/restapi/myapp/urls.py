from django.urls import path
from myapp.views import *


urlpatterns = [
    
    path("create",create),
    path("list",list_data),
    path("update",update),
    path("destroy",destroy),
    
    path("list-student",list_student),
    path("create-student",crate_student),
    path("retrive-student/<id>",retrive_student)
    
    
    
]