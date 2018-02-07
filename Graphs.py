# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:17:35 2018

@author: ucapfh0
"""

import numpy as np


#data=np.loadtxt('data0.txt',delimiter=" ")

data0=data[0::4][:,1]
data1=data[1::4][:,1]
data2=data[2::4][:,1]
data3=data[3::4][:,1]

for x in data0:
    if x == 1:
        

