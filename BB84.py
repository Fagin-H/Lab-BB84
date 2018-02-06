# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales
"""

import numpy as np


data=np.array([[0,1,2,3],[5,5,5,5]])
data20=[]
data21=[]

for i in range(len(data[0])):
    if data[1][i]==5:
        data20.append(data[0][i])
        data21.append(data[1][i])
   
data2=np.array([data20,data21])     
