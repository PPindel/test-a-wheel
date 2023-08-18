from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Review form class
    Allows to write a review
    """
    class Meta:
        model = Review
        fields = ('title', 'service', 'review_text', 'rating')
