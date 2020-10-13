from django.urls import path, include
from . import views
from rest_framework import routers
from django.urls import include
from Visuals.views import CountryViewSet

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet, basename = 'countries')

urlpatterns = [
path('Visuals', views.Visuals, name = 'visuals'),
path('api',include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
