from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name = 'data'),
    # paths for dogs
    path('dogs/', views.dogs_index, name='dogs_index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
    # pats for cats
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
]
