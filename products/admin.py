# Import necessary module and model for admin configuration
from django.contrib import admin
from .models import Product


# Custom Admin configuration for the Product model
class ProductAdmin(admin.ModelAdmin):
    """
    Display fields in the product list view
    """
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

    # Define default sorting order for the product list view
    ordering = ('name',)


# Register the Product model with the custom admin configuration
admin.site.register(Product, ProductAdmin)
