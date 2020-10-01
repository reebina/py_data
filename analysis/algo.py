#!/usr/bin/env python3

# Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow

# For data split 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Algorithims
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


#read data set

data_set = pd.read_csv("data_sets/heart2.csv")

def visualization_correlation_matrix():
    rcParams['figure.figsize'] = 20, 14
    plt.matshow(data_set.corr())
    plt.yticks(np.arange(data_set.shape[1]), data_set.columns)
    plt.xticks(np.arange(data_set.shape[1]), data_set.columns)
    plt.colorbar()

def visualization_histogram():
    data_set.hist()
    
def target_clases():
    rcParams['figure.figsize'] = 8,6
    plt.bar(dataset['target'].unique(), dataset['target'].value_counts(), color = ['red', 'green'])
    plt.xticks([0, 1])
    plt.xlabel('Target Classes')
    plt.ylabel('Count')
    plt.title('Count of each Target Class')

def data_processing():
    data_set = pd.get_dummies(data_set, 
            columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
    
def scale_data():
    standardScaler = StandardScaler()
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])




data = {
      "data_set" : data_set ,
      "data_info" : data_set.info(),
      "data_describe" : data_set.describe(),
      "data_histo" : visualization_correlation_matrix()
        
  } 



        
