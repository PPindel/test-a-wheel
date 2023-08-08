from django.contrib import admin
from .models import Review

# Register the Review model in the admin panel
admin.site.register(Review)

# Define how the Review model will be displayed in the admin list view
list_display = ('title', 'slug', 'status', 'created_on')

# Enable searching for reviews by title and review text
search_fields = ['title', 'review_text']

# Prepopulate the slug field based on the title field
prepopulated_fields = {'slug': ('title',)}

# Add a filter for filtering reviews by their status and creation date
list_filter = ('status', 'created_on')

# Define which field(s) should use the Summernote rich text editor in the admin form  # noqa E501
summernote_fields = ('review_text')
