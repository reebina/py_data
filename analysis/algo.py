#!/usr/bin/env python3

# Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
import seaborn as sb

# For data split 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Algorithim
from sklearn.naive_bayes import GaussianNB

data_set = pd.read_csv("/Users/iamsan/Desktop/py_data/data_sets/heart2.csv")

def target_age():
    '''
    

    Returns
    -------
    seaborn object to demonstrate the distribution of target againts age.

    '''
    sb.set_context(font_scale=1.5, rc = {"font.size" : 6, "axes.titlesize":6, "axes.labelsize": 6})
    return sb.catplot(kind = 'count', data = data_set, x = 'age', hue = 'target',
               order = data_set['age'].sort_values().unique())

def age_sex_target():
    '''
    

    Returns
    -------
    seaborn object to demonstrate barplot of age agains sex with hue as target

    '''
    return  sb.catplot(kind = "bar", data = data_set, y = "age", x = "sex", hue = "target")



def nb_implementation():
    X = data_set.iloc[:, :-1].values
    y = data_set.iloc[:, -1].values
    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state = 0)
    nb = GaussianNB()
    nb.fit(xTrain, yTrain)
    yPredict = nb.predict(xTest)
    
    # Accuracy Score 
    cm = confusion_matrix(yTest, yPredict)
    accuracy_score(yTest, yPredict)
    report = classification_report(yTest, yPredict)
    return report
        

data = {
      "data_set" : data_set,
      "data_describe" : data_set.describe,
      "target_age" : target_age,
      "age_sex_target" : age_sex_target,
      "report" : nb_implementation
        
}

