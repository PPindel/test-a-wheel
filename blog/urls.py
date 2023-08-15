from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # path('post_edit/<slug:slug>/', views.EditTeamAd.as_view(), name='post_edit'),  # noqa E501
    path('post_delete/<slug:slug>/', views.delete_post, name='post_delete'),  # noqa E501
]
