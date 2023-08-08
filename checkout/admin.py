# Import necessary modules and models from Django
from django.contrib import admin
from .models import Order, OrderLineItem


# Inline class for displaying OrderLineItem within OrderAdmin
class OrderLineItemAdminInline(admin.TabularInline):
    # Set the model for the inline class to OrderLineItem
    model = OrderLineItem
    # Specify fields to be displayed as read-only
    readonly_fields = ('lineitem_total',)


# Admin class for configuring the display and behavior of Order model in the admin panel # noqa E501
class OrderAdmin(admin.ModelAdmin):
    # Include the OrderLineItemAdminInline class within the OrderAdmin
    inlines = (OrderLineItemAdminInline,)

    # Specify fields to be displayed as read-only
    readonly_fields = ('order_number', 'date', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    # Specify the layout and order of fields in the edit form
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',
              'grand_total', 'original_bag', 'stripe_pid')

    # Define fields to be displayed in the list view of the admin panel
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    # Specify the default ordering of records in the admin panel
    ordering = ('-date',)


# Register the Order model with the customized admin class (OrderAdmin)
admin.site.register(Order, OrderAdmin)
