from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name = 'data'),
    path('dogs/', views.dogs_index, name='index'),
]
