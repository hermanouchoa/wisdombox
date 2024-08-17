# pip install pandas
# pip install numpy
import pandas as pd
import numpy as np

arr_list = np.array([1,2,3,4,5,6,7,8])
print(arr_list)

arr_zeros = np.zeros((4,6))
print(arr_zeros)

arr_ones = np.ones((4,6))
print(arr_ones)

arr_random = np.random.rand(3,4)
print(arr_random)

print(arr_random.shape)


arr_random_reshape = arr_random.reshape((4,3))
print(arr_random_reshape)


