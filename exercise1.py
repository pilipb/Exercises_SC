# approximating pi with the Leibniz formula

import math

def leibniz(n):
    pi = 0
    for i in range(n):
        sum = 8 / ( (4 * i + 1) * (4 * i + 3))
        pi += sum
    return pi

# calc error from math.pi
def error(pi_n):
    return abs(math.pi - pi_n)

# approximating for n = 100, 1000 and 10000
for n in [100, 1000, 10000]:
    pi_n = leibniz(n)
    print("\nn = %d, pi = %f, error = %f\n" % (n, pi_n, error(pi_n)))

# calculate value of n for error < 0.0000001
n = 1
pi_n = leibniz(n)
while error(pi_n) > 0.0000001:
    n = n * 2
    pi_n = leibniz(n)
print("\nn = %d, pi = %.8f, error = %.8f\n" % (n, pi_n, error(pi_n)))




