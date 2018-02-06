import numpy as np
from BB84 import read_data

data = read_data("countdata.txt")

pulse_data = data[np.isclose(data[:,1],5)] # Select only the rows which correspond to a laser pulse
voltage_steps = np.transpose(np.array((pulse_data[:,0], np.mod(np.arange(pulse_data.shape[0]), 4)))) # Array for converting timestamp to voltage step

count_data = data[np.logical_not(np.isclose(data[:,1],5))][:,1] - 1
times_for_counts = data[np.roll(np.logical_not(np.isclose(data[:,1],5)),-1)]
sorter = np.argsort(voltage_steps[:,0])
time_indices = sorter[np.searchsorted(voltage_steps[:,0], times_for_counts[:,0], sorter=sorter)]
steps_for_counts = voltage_steps[:,1][time_indices]

error_array = np.isclose(count_data, steps_for_counts)
error_rate = np.mean(error_array)

print("Error rate is {}".format(error_rate))
