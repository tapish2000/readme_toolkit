from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='readme-home'),
    path('detail/', views.detail, name='readme-detail'),
    path('detail/installation/', views.installation, name='readme-installation'),
    path('detail/usage/', views.usage, name='readme-usage'),
    path('output/', views.output, name='readme-output'),
    path('download/', views.download, name='readme-download')
]
