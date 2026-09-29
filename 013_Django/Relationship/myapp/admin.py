from django.contrib import admin
from myapp.models import *
# Register your models here.


class ProductDisplay(admin.ModelAdmin):
    list_display=['id','name','price','qty','mfg','brand']
    
    search_fields=['name']
    
    list_filter=['name']
    
admin.site.register(Country)
admin.site.register(Capital)

admin.site.register(Category)
admin.site.register(Product,ProductDisplay)

admin.site.register(Student)
admin.site.register(Course)


