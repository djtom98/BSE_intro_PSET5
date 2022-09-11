# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:23:22 2022

@author: davis
"""

from matplotlib import pyplot as plt
#take average wage dataset
# take unemployment data
#take oil and gas spending per capita/household
#volume of oil consumed by diff sectors
#projected consumption
import pandas as pd
import os
dir=os.getcwd()
path=dir+"\gasindex\Gasoline Index in Europe 2022.xlsx"
print(path)
df=pd.read_csv(path)
print(df)
    
