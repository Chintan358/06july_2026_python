from django.urls import *
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("register",register,name="register"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)