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
        print("Window size not odd number")


if __name__ == "__main__":

    data = [1, 2, 3, 6, 10, 7, 2, 1]
    filter_size = 3

    print(" data : ", data)
    filter_out = signal.medfilt(data, kernel_size = filter_size) 
    print(" medfilt : ", filter_out) 

    median_filter(data, filter_size)

    samplerate, data = wavfile.read("source_hot_fives.wav")
    plt.plot(data)
    plt.show()
