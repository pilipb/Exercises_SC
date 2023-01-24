# Newton’s method is a way of finding the solution x to nonlinear equations of the form
# f(x) = 0. For a single equation, Newton’s method works as follows. First, propose an
# initial guess of the solution x0. Then, create successive approximations to the solution
# using the recursive formula
# xk+1 = xk − f(xk)/f ′(xk)
# until |f(xn)| < ϵ, where ϵ is a small number. The function f ′(x) is the derivative of f(x).

# In this exercise, you will create a Python module called solvers that contains code to
# run Newton’s method. You will then use a Python script to import the module and solve
# the equation f(x) = cos(x) − x = 0.

import numpy as np
import matplotlib.pyplot as plt
from solvers import *

# solve  f(x) = cos(x) − x = 0
# using Newton’s method

f = lambda x: np.cos(x) - x
df = lambda x: -np.sin(x) - 1
x0 = 0.5
tol = 1e-6

x = newton(f, df, x0, tol)
print(x)

# solve using root in scipy
from scipy.optimize import root

sol = root(f, x0)