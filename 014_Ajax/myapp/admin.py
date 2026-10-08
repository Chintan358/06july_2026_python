from django.contrib import admin
from myapp.models import *
# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display = ['name']
    
   

admin.site.register(product,ProductDisplay)

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)