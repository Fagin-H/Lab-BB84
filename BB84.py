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
    indexno5 = np.argwhere(data[:,1]!=5.)
    index5 = np.argwhere(data[:,1]==5.)
    data2 = np.delete(data, indexno5, 0)
    return data2, index5
    
def average_time(only5_data):
    diff=only5_data[:,0]-np.roll(only5_data[:,0],1)
    diff=np.average(diff[1:])
    return diff

def splitdata(data):
    only5_data,index5 = only5(data)
    ave=average_time(only5_data)
    diff=only5_data[:,0]-np.roll(only5_data[:,0],1)
    index = np.argwhere(diff>1.5*ave)
    listindex=index.flatten()
    split_index=np.take(index5,listindex)    
    split_index=split_index.flatten()
    
    
    split_data=np.split(data,split_index)
    return split_data

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
    data2=splitdata(data)#removeDoublePhotonEvents(data))
    return data2


testdata=read_data('4level_200bins_2s_123width.txt')





















