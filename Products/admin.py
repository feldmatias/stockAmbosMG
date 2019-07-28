from django.contrib import admin

from Products.models import Product, ProductColor, ProductSize


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0
    min_num = 1


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 0
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [ProductColorInline, ProductSizeInline]
    search_fields = ['name']
