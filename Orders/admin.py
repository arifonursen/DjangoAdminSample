from django_modern_admin.widgets import ModernSplitDateTime, ModernSelect
from django.contrib import admin
from django.db import models

from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['product', 'orderDate', 'productPrice', 'orderTotal', 'orderQty']
    formfield_overrides = {
        models.DateTimeField: {'widget': ModernSplitDateTime},
        models.ForeignKey: {'widget': ModernSelect},
    }