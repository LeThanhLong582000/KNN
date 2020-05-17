import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split

# Load Data
Data_Frame = pd.read_csv('KNN.csv')
Title_Data = ['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm']

# Normolize Data
for feature in Title_Data:
    Data_Frame[feature] = Data_Frame[feature] / Data_Frame[feature].max()
Data = Data_Frame[Title_Data]
Label = Data_Frame['RainToday']

# Split Data
Data_Train, Data_Test, Label_Train, Label_Test = train_test_split(Data, Label, test_size= 0.2, random_state= 42)
Data_Train = np.array(Data_Train)
Data_Train = np.array(Data_Train)
Data_Test = np.array(Data_Test)
Label_Test = np.array(Label_Test)
Label_Train = np.array(Label_Train)

# Prediction
def Predict(Train, Label, Test, k= 5):
    result = []
    for data in Test:
        Ans = ((Train - data) ** 2).sum(axis= 1)
        K_Min_Value = []
        for i in range(len(Ans)):
            if len(K_Min_Value) < k:
                K_Min_Value.append(i)
            else:
                if Ans[K_Min_Value[-1]] > Ans[i]:
                    K_Min_Value[-1] = i
                    K_Min_Value.sort(key= lambda x: Ans[x], reverse= True)
        KNN_label = Label[K_Min_Value]
        Count_Yes = (KNN_label == 'Yes').sum()
        if Count_Yes > k // 2:
            result.append('Yes')
        else:
            result.append('No')
    return np.array(result)
Label_Predict = Predict(Data_Train, Label_Train, Data_Test, 3)
print(Label_Test)
print(Label_Predict)

# Evaluate
Accuracy = (Label_Predict == Label_Test).sum() / len(Label_Test) * 100
print('Accuracy of KNN: ', Accuracy)

print((Label_Test == 'Yes').sum())
print((Label_Predict == 'Yes').sum())