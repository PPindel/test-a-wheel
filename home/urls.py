from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('403', views.error_403_view, name='403'),
    path('404', views.error_404_view, name='404'),
    path('500', views.handler500, name='500'),
]
