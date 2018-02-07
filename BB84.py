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
    
def no5(data):
    index = np.argwhere(data[:,1]==5.)
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

def joindata(fivedata,no5data):
    data=np.vstack(([no5data,fivedata]))
    return data[np.lexsort(np.fliplr(data).T)]

def removeDoublePhotonEvents(data):
    shiftedPlus = np.append(data[-1:], data[:-1], axis = 0)
    shiftedMinus = np.append(data[1:], data[:1], axis = 0)
    croppedData = data[np.where(
            np.logical_not(
                    np.logical_and(
                            np.logical_or(
                                    np.logical_not(np.isclose(shiftedPlus[:,1],5)),np.logical_not(np.isclose(shiftedMinus[:,1], 5))),
                                    np.logical_not(np.isclose(data[:,1],5)))))]
    return croppedData
 
def fixdata(data):
    data2=joindata(add5(only5(data)),no5(removeDoublePhotonEvents(data)))
    return data2

#testdata=read_data('testdata.txt')




















