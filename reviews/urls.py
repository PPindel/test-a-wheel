from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path('add-review/', views.add_review, name='add_review'),
    path('update-review/<int:review_id>/', views.update_review, name='update_review'),  # noqa E501
    # path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),  # noqa E501
]
