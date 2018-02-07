import numpy as np
from BB84 import read_data

def get_counts_with_voltage_steps(data):
    pulse_data = data[np.isclose(data[:,1],5)] # Select only the rows which correspond to a laser pulse
    voltage_steps = np.transpose(np.array((pulse_data[:,0], np.mod(np.arange(pulse_data.shape[0]), 4)))) # Array for converting timestamp to voltage step

    count_data = data[np.logical_not(np.isclose(data[:,1],5))][:,1] - 1 # Detector counts correspond to not getting a 5
    times_for_counts = data[np.roll(np.logical_not(np.isclose(data[:,1],5)),-1)] # Times are set by entries 1 before the locations of the counts (this is what np.roll does)
    sorter = np.argsort(voltage_steps[:,0]) # The following three lines find the voltage steps corresponding to the count times
    time_indices = sorter[np.searchsorted(voltage_steps[:,0], times_for_counts[:,0], sorter=sorter)]
    steps_for_counts = voltage_steps[:,1][time_indices]
    
    return count_data, steps_for_counts

def basic_error_rate(count_data, steps_for_counts):

    error_list = np.logical_not(np.isclose(count_data, steps_for_counts))
    error_rate = np.mean(error_list)

    print("Basic error rate is {}".format(error_rate))
    
def get_relevant_counts(count_data, steps_for_counts):
    
    count_data = count_data.astype(int)
    count_data = count_data.reshape(count_data.size,1)
    steps_for_counts = steps_for_counts.astype(int)
    
    detectors_for_basis = np.array([[0,1],[0,1],[2,3],[2,3]])
    detection_array = np.isclose(detectors_for_basis[steps_for_counts], count_data)
    detection_list = np.any(detection_array, axis=1)
    counts_to_consider = count_data[detection_list]
    steps_to_consider = steps_for_counts[detection_list]
    counts_to_consider = counts_to_consider.reshape(counts_to_consider.size)
    
    return counts_to_consider, steps_to_consider

def BB84_error_rate(counts_to_consider, steps_to_consider):
    
    error_list = np.logical_not(np.isclose(counts_to_consider, steps_to_consider))
    error_rate = np.mean(error_list)

    print("BB84 error rate is {}".format(error_rate))
    
def channel_error_rate(counts_to_consider, steps_to_consider, n):
    
    counts_of_n = counts_to_consider[np.isclose(steps_to_consider, n)]
    steps_of_n = steps_to_consider[np.isclose(steps_to_consider, n)]
    
    error_list = np.logical_not(np.isclose(counts_of_n, steps_of_n))
    error_rate = np.mean(error_list)
    
    print("Error rate of channel " + str(n) + " is {}".format(error_rate))

if __name__ == "__main__":

    data = read_data("4level_200bins_2s_123width_(0,).txt")
    count_data, steps_for_counts = get_counts_with_voltage_steps(data)
    counts_to_consider, steps_to_consider = get_relevant_counts(count_data, steps_for_counts)
    channel_error_rate(counts_to_consider, steps_to_consider,0)