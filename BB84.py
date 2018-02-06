# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales and cderbz
"""

import numpy as np

def read_data(location):
    data=np.loadtxt(location,delimiter=",")
    data[:,0]=data[:,0]*81*10**-12
    return data

def only5(data):
    index = np.argwhere(data[:,1]!=5.)
    data2 = np.delete(data, index, 0)
    return data2
    
def average_time(only5_data):
    diff=only5_data[:,0]-np.roll(only5_data[:,0],1)
    diff=np.average(diff[1:])
    return diff

def add5(only5_data):

    ave=average_time(only5_data)
    
    diff=only5_data[:,0]-np.roll(only5_data[:,0],1)
    index = np.argwhere(diff>1.5*ave)
    
    listindex=index.flatten()
    
    split_data=np.split(only5_data,listindex)
    newdata=[]
    for sliced in split_data[:-1]:
        newdata.append(sliced)
        newdata.append([sliced[-1,0]+ave,5.])
    newdata.append(split_data[-1])
    return np.vstack(newdata)
    
def fixdata(data):
    return add5(only5(data))