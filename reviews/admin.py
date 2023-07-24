from django.contrib import admin
from .models import Review

admin.site.register(Review)

list_display = ('title', 'slug', 'status', 'created_on')
search_fields = ['title', 'review_text']
prepopulated_fields = {'slug': ('title',)}
list_filter = ('status', 'created_on')
summernote_fields = ('review_text')
