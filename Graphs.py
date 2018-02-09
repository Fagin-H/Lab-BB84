# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:17:35 2018

@author: ucapfh0
"""

import numpy as np
import matplotlib.pyplot as plt
import BB84
import collections as col


def no5(data):
    index5 = np.argwhere(data==5.)
    return np.delete(data, index5, 0)

def group_data(data,n):
    index5 = np.argwhere(data[:]==5.)[:,0]
    index5=index5[:-1]
    return no5(np.take(data[:,1],index5[n::4]+1))

def make_hist(data):
    dic=col.Counter(data)
    return (dic[1]/(dic[1]+dic[2]),dic[2]/(dic[1]+dic[2]),dic[3]/(dic[3]+dic[4]),dic[4]/(dic[3]+dic[4]))



def save_figs(data,location):
    k=0
    data_fixed=BB84.fixdata(data)
    for data_n in data_fixed:
        k+=1
        for i in range(4):
            hist_data=make_hist(group_data(data_n,i))
            objects = np.arange(4)+1
            y_pos = np.arange(len(objects))             
            plt.bar(y_pos, hist_data, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.savefig(location+'/'+str(k)+str(i+1)+'.png')
            plt.close()

if __name__=='__main__':
    data=np.loadtxt('data40.txt',delimiter=" ")
    save_figs(data,'real_data_bar_plots')