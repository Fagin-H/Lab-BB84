# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales
"""

import numpy as np

def read_data(location):
    return np.loadtxt(location,delimiter=",")


def average_time(data):
    index = np.argwhere(data[:,1]!=5.)
    data2 = np.delete(data, index, 0)
    diff=data2[:,0]-np.roll(data2[:,0],1)
    diff=np.average(diff[1:])
    return diff*81*10**-12

data=read_data('testdata.txt')

