from django.shortcuts import render
import pandas as pd
import os
import numpy as np
from .models import Country, CountryManager
from django.core.files import File
from Visuals.serializers import CountrySerializer
from rest_framework import viewsets
from rest_framework.response import Response
import requests

def Visuals(request):
    Country.objects.edit_country_name('United States Virgin Islands', 'Mohaned')
    return render(request, 'Home.html')

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
