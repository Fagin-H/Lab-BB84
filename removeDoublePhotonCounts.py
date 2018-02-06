from BB84 import read_data
import numpy as np

def removeDoublePhotonEvents(data):
    shiftedPlus = np.append(data[-1], data[:-1])
    shiftedMinus = np.append(data[1:], data[0])
    croppedData = data[np.where(np.logical_not(np.logical_and(np.logical_or(np.isclose(data,shiftedPlus),np.isclose(data, shiftedMinus)), np.logical_not(np.isclose(data,5)))))]
    return croppedData

data = read_data('count_data.txt')
croppedData = removeDoublePhotonEvents()