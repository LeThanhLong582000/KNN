import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

# Load csv
Data_Frame = pd.read_csv('weatherAUS.csv')

# Feature and length
Title = list(Data_Frame.head(1))
for Feature in Title:
    print('Feature', Feature, 'has', len(Data_Frame[Feature]), sep = ' ')
print()

# Categorical data and numerical data 
categorical_data = []
numerical_data = []
for Feature in Title:
    if type(Data_Frame[Feature][0]) == str:
        categorical_data.append(Feature)
    else:
        numerical_data.append(Feature)
print('categorical data:')
print(categorical_data)
print('numerical data:')
print(numerical_data)
print()

# Count missing value
for Feature in Title:
    Null_Value = Data_Frame[Feature].isnull().sum()
    print('Feature', Feature, 'has', Null_Value, 'missing value', sep = ' ')
print()

# Filling missing data
for Feature in Title:
    Data_Frame[Feature].fillna(Data_Frame[Feature].mode()[0], inplace= True) # Replace nan by mode of data
print()

# Histogram data
for i in range(0, len(numerical_data), 4):
    fig = plt.figure('Histogram data', figsize= (14, 9))
    for j in range(i, min(i + 4, len(numerical_data))):
        ax = plt.subplot(2, 2, j % 4 + 1)
        ax.hist(Data_Frame[numerical_data[j]], bins= 50)
        plt.title(numerical_data[j], fontsize= 10)
        plt.xlabel('value')
        plt.ylabel('Times of appearance')
    plt.show()
Data_Frame.hist(bins= 50, figsize= (15, 9))
plt.show()

# Heat Map
Data = Data_Frame[['MinTemp', 'MaxTemp', 'WindSpeed9am', 'Humidity9am']]
Data.plot(kind= 'scatter', x= 'MinTemp', y= 'MaxTemp', alpha= 0.3, s= Data['WindSpeed9am'], label = 'Humidity9am',
            c= 'Humidity9am', figsize= (15, 9), colorbar= True, cmap= plt.get_cmap('jet'))
plt.legend()
plt.show()