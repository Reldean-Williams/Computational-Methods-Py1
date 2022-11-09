import numpy as np


def mse(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    square_root = np.square(np.subtract(actual, predicted))
    return square_root.mean()
    
actual = [1, 3, 5, 7, 9]
predicted = [2, 4, 6, 8, 10]

print(mse(actual, predicted))

