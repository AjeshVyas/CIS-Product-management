from django.contrib import admin

from management.models import Product, Category
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','tags','category','user')
    search_fields = ('id','name','tags','category__name','user__username')

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')