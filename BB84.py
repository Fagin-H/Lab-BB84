# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:51 2018

@author: fhales
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
    
def average_time(data):
    diff=data[:,0]-np.roll(data[:,0],1)
    diff=np.average(diff[1:])
    return diff



data=only5(read_data('testdata.txt'))

ave=average_time(data)

diff=data[:,0]-np.roll(data[:,0],1)
index = np.argwhere(diff>1.5*ave)

listindex=[]
for x in index:
    listindex.append(x[0])

data2=np.split(data,listindex)
newdata=data2[0]
for i in range(len(data2)):
    newdata=np.hstack(newdata,newdata[-1]+ave)
    newdata=np.hstack(newdata,data2[i])


