from .models import Post
from django import forms
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.db import models


class PostForm(forms.ModelForm):
    """
    Review form class
    Allows to write a review
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'section', 'content', 'excerpt', 'image', 'status')  # noqa E501
