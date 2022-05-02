# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:29:03 2022

@author: jonat
"""

import pandas as pd

data = {'Name':['Renault', 'Duster', 'Maruti', 'Honda City'], 'Ratings':[9.0, 8.0, 5.0, 3.0]}  

df = pd.DataFrame(data, index = ['position 1', 'position 2', 'position 3', 'position 4'])

for index, row in df.iterrows():
    if(row.Ratings == 8):
        print("igual")
    print(row.Ratings)
