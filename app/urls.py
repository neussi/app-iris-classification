# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('predict/', views.PredictView.as_view(), name='predict'),
    path('species-info/<str:species_name>/', views.SpeciesInfoView.as_view(), name='species_info'),
    path('species-info/', views.SpeciesInfoView.as_view(), name='species_info_post'),
]