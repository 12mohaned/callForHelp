from django.urls import path, include
from . import views

urlpatterns = [
path('Visuals', views.Visuals, name = 'visuals')
]
