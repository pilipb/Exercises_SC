import numpy as np

# define vectors
vec_a = np.array([1, 2, 3])
vec_b = np.array([6, 5, 4])

# function to return the dot product of two vectors
def dot_product(a, b):
    return np.dot(a, b)

# define matrices
mat_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# function to return the product of two matrices
def matrix_product(a, b):
    try:
        return a*b
    except ValueError:
        print("Matrices cannot be multiplied")

print(matrix_product(mat_a, mat_b))

