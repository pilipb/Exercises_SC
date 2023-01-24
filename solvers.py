# In this file, write a Python function that implements Newton’s method using the recursive
# formula above. Note: your module should not run Newton’s method; this is what
# the script is for (see part (b)).

def newton(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x)/df(x)
    return x

# implement the biscetion method

def bisect(f, a, b, tol):
    x = (a + b) / 2
    while abs(f(x)) > tol:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
    return x

# implement the secant method

def secant(f, x0, x1, tol):
    x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    while abs(f(x)) > tol:
        x0 = x1
        x1 = x
        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    return x
    