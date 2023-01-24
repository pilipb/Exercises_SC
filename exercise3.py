import numpy as np

array_1   = np.array([5, 4, 9, 2, 0, 4, 7, 2])

# print the last element of the array
print(array_1[-1])

print(array_1[1:6]) # print the elements from index 1 to 5

print(array_1[:-2]) # all elements except the last two

print(array_1[::2]) # every second element

# change last element to 9
array_1[-1] = 9
print(array_1)

array_1[0:3] = 1 # change first three elements to 1
