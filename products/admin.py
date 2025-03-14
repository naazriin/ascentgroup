from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'created_at', 'updated_at', 'is_active']