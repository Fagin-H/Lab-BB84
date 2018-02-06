# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales
"""

import numpy as np


data=np.array([[0,1,2,3],[5,1,5,5]])

index = np.argwhere(data[1]!=5)
data2 = np.delete(data[0], index)
print(data2)