from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
