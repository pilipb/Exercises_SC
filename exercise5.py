#  solving linear system of equations

import numpy as np

# define the matrix

A = np.array([[1, 0, 0, 0], [1, -2, 1, 0 ], [0, 1, -2, 1], [0, 0, 0, 1]])

b = np.array([0,1,1,2])

# solve the system

x = np.linalg.solve(A, b)
print(x) 

# explain the result

# The result is a vector of the form [a, b, c, d] where a, b, c and d are the coefficients of the equation
# 0 = a + b - c + d
# 1 = a - 2b + c - d
# 1 = b - 2c + d
# 2 = d
