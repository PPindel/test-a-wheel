# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User

# Choices for the 'status' field
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Define the 'Post' model
    """

    # Choices for the 'section' field
    SECTIONS = [
        ('Cars', 'Cars'),
        ('Tips', 'Tips'),
        ('Guides', 'Guides'),
    ]

    # Fields of the 'Post' model
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    section = models.CharField(max_length=25, choices=SECTIONS, default='Cars')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']  # Order posts by creation date in descending order # noqa E501

    def __str__(self):
        return self.title  # Return the title of the post when displayed as a string # noqa E501

    def number_of_likes(self):
        return self.likes.count()  # Calculate and return the number of likes for the post # noqa E501
