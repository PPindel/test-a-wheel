# Import necessary module and model from Django
from django import forms
from .models import Order


# Form class for creating and customizing Order form
class OrderForm(forms.ModelForm):
    class Meta:
        # Set the model to use for the form
        model = Order
        # Specify the fields to include in the form
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Customize form by adding placeholders, classes,
        removing labels, and setting autofocus
        """
        super().__init__(*args, **kwargs)

        # Define placeholders for form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set autofocus on the 'full_name' field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Customize each field's placeholder and classes
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'

            # Remove labels from fields
            self.fields[field].label = False
