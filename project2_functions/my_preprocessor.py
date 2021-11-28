# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:54:16 2021

@author: sssalas
"""
import pandas as pd
from sklearn import preprocessing


def my_scaler(train, test):
    """standardization of train and test data"""
    df_1 = pd.DataFrame(train)
    df_1_columns = df_1.columns # Get column names first
    scaler = preprocessing.StandardScaler() # Create the Scaler object
    df_1 = scaler.fit_transform(df_1) # Fit your data on the scaler object
    df_1 = pd.DataFrame(df_1, columns=df_1_columns)

    df_2 = pd.DataFrame(test)
    df_2_columns = df_2.columns # Get column names first
    df_2 = scaler.fit_transform(df_2) # Fit your data on the scaler object
    df_2 = pd.DataFrame(df_2, columns=df_2_columns)
    
    return df_1, df_2

