# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:54:16 2021

@author: sssalas
"""
from matplotlib import pyplot as plt

def my_count_plot(train,Cover_Type):
	train.Cover_Type.value_counts().plot(kind="bar")

def my_dist_plot(train,Cover_Type):
    train.groupby("Cover_Type").boxplot(rot=90)
    plt.rcParams["figure.figsize"] = (8,8)
    
def my_plot_size_default():
    plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

def my_coef_plot(data,model,row_index):
    """Create a horizontal bar chart for coefficients from a given model"""
    fig=plt.figure(figsize=(20,15), dpi= 100)
    plt.barh(data.columns, model.coef_.tolist()[row_index])
    plt.yticks(fontsize=14)
    plt.show(fig)
    
def my_coef_plot_multi(X_train_multi,model,row_index):
    fig=plt.figure(figsize=(8,8), dpi= 60)
    plt.title(f'Coefficients for Cover_Type {row_index+1}', fontsize=20)
    plt.barh(X_train_multi.columns, model.coef_.tolist()[row_index])
    plt.yticks(fontsize=11)
    plt.show(fig)