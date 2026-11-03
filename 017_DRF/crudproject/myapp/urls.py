from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("categories",CategoryViewSet,basename="category")
router.register("products",ProductViewSet,basename="product")

urlpatterns = [
    path("",include(router.urls))
]