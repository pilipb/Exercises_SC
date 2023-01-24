# In this file, write a Python function that implements Newton’s method using the recursive
# formula above. Note: your module should not run Newton’s method; this is what
# the script is for (see part (b)).

def newton(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x)/df(x)
    return x
    