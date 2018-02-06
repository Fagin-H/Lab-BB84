# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales
"""

import numpy as np

def read_data(location):
    return np.loadtxt(location,delimiter=",")

data=np.array([[0,1,2,3,4,5,6],[5,5,5,5,5,5,5]])

index = np.argwhere(data[1]!=5)
data2 = np.delete(data[0], index)
diff=np.hstack((data2,[0]))-np.hstack(([0],data2))
diff = np.delete(diff, 0)
diff=diff[:-1]
diff=np.average(diff)
print(diff)