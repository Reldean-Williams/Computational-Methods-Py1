import numpy as np

def median_filter(data, filter_size):
    data = [1, 2, 3, 6, 10, 7, 1]                       
    N = len(data)
    filter_size = sorted(data)
    indexer = (filter_size - 1) // 2
    med_filter = (data[0])
    padding = np.zeros((N, len(data[0])))
    for i in range(0, N - 2):
       print(data[i], data[i + 1], data[i + 2])
       x = median_filter(data[i], data[i + 1], data[i + 2])
    med_filter.append(x)
    med_filter.append(data(-1))
    print(med_filter)



