# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:17:35 2018

@author: ucapfh0
"""

import numpy as np
import matplotlib.pyplot as plt


def no5(data):
    index5 = np.argwhere(data==5.)
    return np.delete(data, index5, 0)


#data=np.loadtxt('data0.txt',delimiter=" ")
index5 = np.argwhere(data[:]==5.)[:,0]
index5=index5[:-1]
data1=no5(np.take(data[:,1],index5[3::4]+1))




plt.hist(data1)
plt.show
