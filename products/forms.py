# Import necessary modules and model for the product form
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Custom form for creating and updating Product instances
    """

    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the Product model

    image = forms.ImageField(label='Image',  # Custom label for the image field
                             required=False,  # Image is not required
                             widget=CustomClearableFileInput)  # Use custom widget for file input  # noqa E501

    def __init__(self, *args, **kwargs):
        # Initialize the form with appropriate attributes
        super().__init__(*args, **kwargs)

        # Customize the widget attributes for each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
