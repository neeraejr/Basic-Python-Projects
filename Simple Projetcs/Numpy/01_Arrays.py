import numpy as np


arr = np.array([1,2,3])
print("1D Array: ",arr)


arr_2 = np.array([[1,2,3],[4,5,6]])
print("2D Array: ",arr_2)

arr_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D Array: ",arr_3)

zeroes = np.zeros((3,3))
print("Zeroes Array: ",zeroes)

random_arr = np.random.rand(3,3)
print("Random Array: ",random_arr)

