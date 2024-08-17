# pip install pandas
# pip install numpy
import pandas as pd
import numpy as np

#trabalhando com array usando numpy
arr_list = np.array([1,2,3,4,5,6,7,8])
print(arr_list)

#criando arrays de zeros
arr_zeros = np.zeros((4,6))
print(arr_zeros)

#criando arrays de um
arr_ones = np.ones((4,6))
print(arr_ones)

#criando arrays com numeros randomicos
arr_random = np.random.rand(3,4)
print(arr_random)

print(arr_random.shape)

arr_random_reshape = arr_random.reshape((4,3))
print(arr_random_reshape)

# união de arrays
print("união de arrays")
arr1 = np.array([[1,2],[3,4]])
print("arr1")
print(arr1)
arr2 = np.array([[5,6],[7,8]])
print("arr2")
print(arr2)
arr3 = np.array([[9,10],[11,12]])
print("arr3")
print(arr3)

arr4 = np.concatenate((arr1, arr2, arr3), axis=1)
print("arrays unidos - axis=1")
print(arr4)

arr5 = np.concatenate((arr1, arr2, arr3), axis=0)
print("arrays unidos - axis=0")
print(arr5)

#separando arrays
print("separando arrays")
arr4_aplit = np.split(arr4, 2)
print("arr4 split")
print(arr4_aplit)

#tranposição de matrizes
arr4_transpose = np.transpose(arr4)
print("array transposto")
print(arr4_transpose)

#reverter transposição
arr4_reversao_tranpose = arr4_transpose.T
print("reversão tranposição")
print(arr4_reversao_tranpose)

# soma de matrizes
arr_a = np.array([1,7,27])
print("arr_a")
print(arr_a)
arr_b = np.array([1,5,1])
print("arr_b")
print(arr_b)

print("soma de array")
arr_a_b = np.add(arr_a,arr_b)
print(arr_a_b)

#subtração de matrizes
arr_sub_a_b = np.subtract(arr_a,arr_b)
print("subtração de array")
print(arr_sub_a_b)
