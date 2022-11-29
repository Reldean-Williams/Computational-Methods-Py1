import numpy as np
import unittest
from scipy import signal as sc
from scipy.io import wavfile
import matplotlib.pyplot as plt
import Median_Filter as median
from scipy.io.wavfile import write
import time
from scipy import signal as sc
from tqdm import tqdm
from playsound import playsound

def get_filter_len(degraded1):

    '''
    By computing the minimum MSE the get_filter_len gives the best filter 
    length for degraded audio.
   

    Returns the filter length.

            Input:
                    degraded1  (array)  : degraded audio

            Output:
                    filter_len  (int)    : filter length 
    '''

    # Computing the MSE for the window size from 7 to 
    filter_sizes = [7,9,11,13,15,17,19,21,23]

    MSE = np.zeros(len(filter_sizes))

    Threshold = 32000

    for w in range(len(filter_sizes)):
        
        filter_size = filter_sizes[w]	
        padding = (filter_size - 1) // 2
 
        for index in range(len(degraded1)):
            if( abs(degraded1[index]) >= Threshold ):            
                res_data[index] = median.median_filter(degraded1[index - padding : index + padding + 1], filter_size)

        MSE[w] =  np.square(np.subtract(original1,res_data)).mean()

    
    
    # Returns a minimum index MSE
    min_index = np.where(MSE == MSE.min())

    # Converts it into an integer value
    min_i = int(min_index[0])
    
    # Stores the minimum filter length
    filter_len = filter_sizes[min_i] 

    plt.plot(filter_sizes,MSE,'-r*')
    plt.xlim(1,20,1)
    plt.ylim(0.4,1.8)
    plt.xlabel("Filter Length")
    plt.ylabel("MSE")
    plt.title("MSE vs Filter Size")
    plt.show()

    return filter_len

if __name__ == "__main__":

    # Reading data from the Audio files
    samplerate, original = wavfile.read("source_hot_fives_.wav")
    samplerate, degraded = wavfile.read("deg_.wav")

    # Using a single channel 
    original1 = original[:, 1]
    degraded1 = degraded[:, 1]

    # Creating an Array of detect for the position of clicks
    detect = np.zeros(len(degraded1))

    Threshold = 32000
    for i in range(len(degraded1)):
        if( abs(degraded1[i]) >= Threshold ):
            detect[i] = 1

    # Plotting the original, degraded and detected clicks
    figure, axs = plt.subplots(3, 1)
    axs[0].plot(original1)
    axs[0].set_title('Original Audio')
    axs[1].plot(degraded1)
    axs[1].set_title('Degraded Audio')
    axs[2].plot(detect)
    axs[2].set_title('Clicks')

    for ax in axs.flat:
        ax.label_outer()

    plt.show()


    # Creating a copy of degraded data
    res_data = degraded1

    degraded1 = degraded1.tolist()

    # Computing the best filter length
    filter_size = get_filter_len(degraded1)

    # print(" Best filter len : ",window)

    # Adding a data point before and after the click to find the median of data
    padding = (filter_size - 1) // 2

    start = time.time()

    for index in range(len(degraded1)):
        if( detect[index] == 1 ):
            res_data[index] = median.median_filter(degraded1[index - padding : index + padding + 1], filter_size)

    stop = time.time()  

    print(" Execution time for Median Filter : ", format(stop - start))

    # Plotting original, degraded and restored audio data
    figure, axs = plt.subplots(3, 1)
    axs[0].plot(original1)
    axs[0].set_title('Original Audio')
    axs[1].plot(degraded1)
    axs[1].set_title('Degraded Audio')
    axs[2].plot(res_data)
    axs[2].set_title('Restored Audio - Median Filter')

    for ax in axs.flat:
        ax.label_outer()

    plt.show()

    # Writing the restored data to create an output audio file
    res_data1 = np.array(res_data)
    write("output_median_filter.wav", samplerate, res_data1.astype(np.int16))

    # Playing the Output Audiio sound 
    playsound("output_median_filter.wav")

Test_data = [1, 7, 11, 4, 2]
filter_size = 5

class TestCode(unittest.TestCase):
    def Test_median_filter(self):
        median_val = median.median_filter(Test_data, filter_size)
        median_scipy_array = sc.signal.medfilt(Test_data, kernel_size = 5)

        med = median_scipy_array[len(median_scipy_array) // 2 + 1]

        check = np.array(median_val, med)

unittest.main()
