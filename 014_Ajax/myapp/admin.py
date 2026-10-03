from django.contrib import admin
from myapp.models import product
# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display = ['name']
    
   

admin.site.register(product,ProductDisplay)
