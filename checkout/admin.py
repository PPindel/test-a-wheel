# Import necessary modules and models from Django
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline class for displaying OrderLineItem within OrderAdmin
    """

    # Set the model for the inline class to OrderLineItem
    model = OrderLineItem
    # Specify fields to be displayed as read-only
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for configuring the display and behavior of Order model in the admin panel # noqa E501
    """

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
              'grand_total', 'original_bag', 'stripe_pid', 'status')

    # Define fields to be displayed in the list view of the admin panel
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    # Specify the default ordering of records in the admin panel
    ordering = ('-date',)


# Register the Order model with the customized admin class (OrderAdmin)
admin.site.register(Order, OrderAdmin)
