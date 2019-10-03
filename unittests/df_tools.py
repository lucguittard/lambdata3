"""
pack2 - a limited set of df engineering tools
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# code to train/test/val split a df

def splitter(df):
    train, test = train_test_split(df, train_size=.8)
    train, val = train_test_split(train, train_size=.8)
    print(train, test, val)

def detail_na(df):
    nas = df.isna().sum()
    print(nas)

def null(X):
    null_list = X.isnull().sum()
    return null_list

# code to make a class

class Complex:
    """
    Class for complex numbers
    """
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    """
    Method to add together two complex numbers
    """
    def addition(self, added):
        self.add = (self.r+self.i)
