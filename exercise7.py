#  The Moore–Penrose inverse, or pseudoinverse, provides a means to define the inverse of
# singular and non-square matrices. For a matrix A with linearly independent columns, 
# the Moore–Penrose inverse is defined as the matrix A+ that satisfies the equation
# A+ = (AT A)−1 AT

# write a function that takes a matrix A as input and returns the Moore–Penrose inverse of A

import numpy as np

def moore_penrose_inverse(A):
    return np.linalg.pinv(A)
    

    # manually:
def pseudoinverse(A):
    
    # compute transpose of A
    A_T = np.transpose(A)

    # compute the inverse of A_T*A
    A_T_A_inv = np.linalg.inv(np.dot(A_T, A))

    return np.dot(A_T_A_inv, A_T)


A = np.array([[1,-1],[2,4],[1,1],[3,8]])

Aplus = moore_penrose_inverse(A) 
# Aplus = pseudoinverse(A)

print(np.round(np.dot(Aplus, A),2))

# consider over determined system of equations:

b = np.array([2,4,6,8])

# Use the pseudoinverse to compute the solution x. Hint: left multiply the system of
# equations Ax = b by A+ and use A+A = I to show that x = A+b.

x = np.dot(Aplus, b)
print(x)

# More specifically, the vector x = A+b minimises
# the error ||Ax−b||, where ||·|| is the Euclidean norm. Minimising ||Ax−b|| is known
# as a least-squares problem.

