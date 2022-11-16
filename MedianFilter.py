from sympy import array
import numpy as np

def median_filter(data, filter_size):
    data = filter_size / 2
    padding = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

     #arr = []
#removed_noise = median_filter(arr, 5)