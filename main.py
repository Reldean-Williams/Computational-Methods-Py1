import numpy as np


def mse(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    square_root = np.square(np.subtract(actual, predicted))
    return square_root.mean()
    
actual = [1, 3, 5, 7, 9]
predicted = [2, 4, 6, 8, 10]

print(mse(actual, predicted))

def sum():
  numbers = input("The sum of the first N odd natural numbers")
  
  for i in range(1, n+1)

