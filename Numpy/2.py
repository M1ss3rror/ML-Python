import numpy as np
import os
os.system('cls')
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(f'arrayl + array2={array1 + array2}')

array3 = np.array([[7, 8, 9], [3, 2, 1]])
print(f'array3 + array1={array3 + array1}')

array = np.array([[1, 2, 3], [4, 5, 6]])
center_array = array[:,2]
center_array += 100
print(f'center_array=/n{center_array}')
print(f'array=/n{array}')

array2 = np.array([[1, 2, 3], [4, 5, 6]])
second_row = array2[1] .copy()
second_row += 100
print(f'second_row=\n{second_row}')
print(f'array2=\n{array2}')