# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:11:01 2021

@author: sssalas
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures as plf


def my_dummy(train, test, cols):
    """This function takes train and test data (or any two data frames)
    and the list of columns that will be transformed into dummies"""
    cols = ['Wilderness_Area', 'Soil_Type']
    train_d = pd.get_dummies(train, columns=cols,drop_first=True)
    test_d = pd.get_dummies(test, columns=cols,drop_first=True)
    return train_d, test_d


def my_total_transformer_bi(test):
    """This function applies all that we applied to the train data in project 2.
    This creates dummy variables while avoiding the dummy variable trap.
    This function also generates polynomial feature of order 2"""
    poly = plf(2)
    X_test_d = test[['Wilderness_Area', 'Soil_Type']]
    X_test_d_bi = pd.get_dummies(X_test_d, columns=['Wilderness_Area', 'Soil_Type'],drop_first=True)
    X_test_d_columns_bi = X_test_d_bi.columns
    X_test_f = test.drop(['Wilderness_Area', 'Soil_Type'], axis=1)
    X_test_f_bi = poly.fit_transform(X_test_f)
    X_test_f_columns_bi = np.array(poly.get_feature_names(X_test_f.columns))
    X_test_columns_bi = np.concatenate([X_test_f_columns_bi, X_test_d_columns_bi])
    final_X_test_bi = np.concatenate((X_test_f_bi, X_test_d_bi), axis=1)
    final_X_test_bi = pd.DataFrame(final_X_test_bi)
    final_X_test_bi.columns = X_test_columns_bi
    final_X_test_bi = final_X_test_bi.drop(['1'],axis=1)
    return final_X_test_bi

#def my_total_transformer_multi(test):
    #potential = ['Wilderness_Area', 'Soil_Type']
    #X_test_d_multi = test[potential]
    #X_test_d_multi = pd.get_dummies(X_test_d_multi, columns=potential,drop_first=True)
    #X_test_d_columns_multi = X_test_d_multi.columns
    
    #poly = plf(2)
    #X_test_f_multi = test.drop(['Wilderness_Area', 'Soil_Type'], axis=1)
    #X_test_f_multi_1 = poly.fit_transform(X_test_f_multi)
    #X_test_f_columns_multi = np.array(poly.get_feature_names(X_test_f_multi.columns))
    #X_test_columns_multi = np.concatenate([X_test_f_columns_multi, X_test_d_columns_multi])
    #final_X_test_multi = np.concatenate((X_test_f_multi_1, X_test_d_multi), axis=1)
    #final_X_test_multi = pd.DataFrame(final_X_test_multi)
    #final_X_test_multi.columns = X_test_columns_multi
    #final_X_test_multi = final_X_test_multi.drop(['1'],axis=1)
    #return final_X_test_multi



#def my_binary_encoder(train,cols,a):
    #df = pd.DataFrame(train)
    #cols = df[column]
    #for q in df.column:
        #if q < a:
            #df['cols']  = 1
        #else:
            #df['cols']  = 0
    #return df
    #X_train_bi['Cover_Type'] = [1 if q >= 7 else 0 for q in train.Cover_Type ]


