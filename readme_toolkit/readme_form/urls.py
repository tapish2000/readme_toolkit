from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='readme-home'),
    path('installation/', views.installation, name='readme-installation'),
    path('usage/', views.usage, name='readme-usage'),
]
