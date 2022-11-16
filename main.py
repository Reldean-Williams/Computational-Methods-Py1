from ast import Num
import numpy as np

def mse(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    square_root = np.square(np.subtract(actual, predicted))
    return square_root.mean()
    
actual = [1, 3, 5, 7, 9]
predicted = [2, 4, 6, 8, 10]

print(mse(actual, predicted))

#def sum():
numbers = int(input("The sum of the first N odd natural numbers: "))
sum = 0
num = 1
while num <= numbers:
    if num%2 == 1:
     sum = sum + num
    num = num + 2
    print("Odd numbers", sum)
