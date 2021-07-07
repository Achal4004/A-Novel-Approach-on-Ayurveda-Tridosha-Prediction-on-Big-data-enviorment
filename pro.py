
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('file1.csv')
dataset.isnull().sum()

X = dataset.iloc[:, 0:54].values
y = dataset.iloc[:, -1].values
 

classifier.score(X_train, y_train)
classifier.score(X_test, y_test)

from sklearn.metrics import confusion_matrix,recall_score,precision_score
con=confusion_matrix( y_train, y_test)
recall_score( y_train, y_test,average='micro')
precision_score( y_train, y_test,average='micro')

