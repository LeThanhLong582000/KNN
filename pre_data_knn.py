import numpy as np 
import pandas as pd

Data_Frame = pd.read_csv('weatherAUS.csv')
Title = ['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'RainToday']
Data = Data_Frame[Title]

for feature in Title:
    Index = Data_Frame[feature].notnull()
    Data = Data[Index]

Data = Data.head(2000)
Data.to_csv('KNN.csv', index= False)