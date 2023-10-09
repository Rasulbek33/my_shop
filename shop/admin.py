from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name','slug']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name','slug','price',
                    'available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']
    
