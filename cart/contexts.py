# Import necessary modules
from decimal import Decimal  # noqa
from django.conf import settings  # noqa
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Function to calculate and return cart contents for rendering in templates
    """

    cart_items = []  # List to store cart item details
    total = 0  # Initialize total cost of items in the cart
    product_count = 0  # Initialize total quantity of products in the cart
    cart = request.session.get('cart', {})  # Get the current cart dictionary from session # noqa E501

    # Loop through items in the cart dictionary
    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            # Fetch the corresponding 'Product' object using its primary key (item_id) # noqa E501
            product = get_object_or_404(Product, pk=item_id)

            # Calculate the cost of the current item and add to the total
            total += item_data * product.price

            # Increase the product count by the quantity of the current item
            product_count += item_data

            # Append item details to the cart_items list
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    grand_total = total  # Grand total is the same as the calculated total in this case # noqa E501

    # Create a dictionary context containing all the calculated values and cart item details # noqa E501
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context  # Return the context dictionary containing cart information
