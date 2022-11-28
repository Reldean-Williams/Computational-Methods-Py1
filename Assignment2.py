import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

def median_filter(data, filter_size):

    if(filter_size % 2 == 1):
        padded_data = data
        length = len(data)
        median_array = []
        padding = (filter_size - 1) // 2
        print("padding: ", padding)

        for i in range(padding):
            padded_data.insert(0, 0)
            
        for i in range(padding):
            padded_data.insert(len(padded_data), 0)

        for index in range(length):

            filter_size_array = padded_data[index: filter_size + index]
            filter_size_array.sort()     

            median = filter_size_array[int((filter_size - 1) / 2)]

            median_array.append(median)

        return median_array
    else:
        print("The filter_size is not odd")

samplerate, original = wavfile.read("source_hot_fives_.wav")
original = original[:,1]
plt.plot(original)
plt.title("Original Audio")
plt.show()

samplerate, degraded = wavfile.read("deg_.wav")
degraded = degraded[:,1]
plt.plot(degraded)
plt.title("Degraded Audio")
plt.show()

