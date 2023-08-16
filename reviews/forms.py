from .models import Review
from django import forms
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.db import models


class ReviewForm(forms.ModelForm):
    """
    Review form class
    Allows to write a review
    """
    class Meta:
        model = Review
        fields = ('title', 'service', 'review_text', 'rating')
