from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Register the 'Review' model with the admin site
    """

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'review_text']
    list_filter = ('status', 'created_on')
    summernote_fields = ('review_text',)
