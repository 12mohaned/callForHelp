from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import urllib, base64
dataframe =pd.read_csv(os.path.join(r"C:\Users\mohan\Machine-learning-models\datasets",'share-deaths-suicide.csv'))
years =  np.unique(dataframe['Year'])
countries = np.unique(dataframe['Entity'])

def view_countryRate(country_name):
    country_deaths = []
    Query = dataframe.where(dataframe['Entity'] == country_name)
    for i in Query['Deaths']:
        if(i > 0 or i <= 100):
            country_deaths.append(i)
    if len(country_deaths) == 0:
        return 'No Country with that Name'
    plot_country(country_name, country_deaths)

#view the death rate of all countries
def view_agg():
    countries_deaths = {}
    for i in countries:
        countries_deaths[i] = view_countryRate(i)
    return countries_deaths

def plot_country(country_name, country_deaths):
    plt.plot(years,country_deaths, color = 'blue')
    plt.title(country_name + ' suicide rates')
    buffer = io.BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return uri
def Visuals(request):
    uri = view_countryRate('Afghanistan')
    print(uri)
    return render(request, 'Home.html',{'data':uri})
