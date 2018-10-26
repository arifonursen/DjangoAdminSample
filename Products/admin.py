from django.contrib import admin
from django.db import models

from django_modern_admin import widgets

from .models import Products, OtherProducts


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(OtherProducts)
class OtherProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']