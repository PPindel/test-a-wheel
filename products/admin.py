from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'rating',
        'image',
        'history_check',
        'garage_check',
        'premium_check',
        'extra_warranty',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
