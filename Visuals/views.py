from django.shortcuts import render
import pandas as pd
import os
import numpy as np
from .models import Country
dataframe =pd.read_csv(os.path.join(r"C:\Users\mohan\Machine-learning-models\datasets",'share-deaths-suicide.csv'))
countries = np.unique(dataframe['Entity'])

def Visuals(request):
    return render(request, 'Home.html')
