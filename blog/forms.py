from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """
    Review form class
    Allows to write a review
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'section', 'content', 'excerpt', 'image', 'status')  # noqa E501
