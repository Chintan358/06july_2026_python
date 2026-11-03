from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employess",EmployeeViewSet,basename='employee')




urlpatterns = [
    
    path('', include(router.urls)),
    
    path("create",create),
    path("list",list_data),
    path("update",update),
    path("destroy",destroy),
    
    path("list-student",list_student),
    path("create-student",crate_student),
    path("retrive-student/<id>",retrive_student),
    path("update-student/<id>",update_student),
    path("patch-student/<id>",patch_student),
    path("delete-student/<id>",delete_student),
    
    
    path("products/",ProductView.as_view()),
     path("products/<id>/",ProductViewById.as_view()),
        
    
    
    
]