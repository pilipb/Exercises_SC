# Use NumPy’s linspace function to create an array called t that contains 500 values
# between 0 and 5. Create a second array called y that stores the values of y = t^2e^-2t

import numpy as np

t = np.linspace(0, 5, 500)
y = t**2 * np.exp(-2*t)

# Plot y as a function of x. Add labels to the x and y axes. Edit the line colour and
# thickness and font sizes to your preference.

import matplotlib.pyplot as plt

plt.plot(t, y, color='red', linewidth=2)
plt.xlabel('t', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()

# Find the maximum value of y. Note: this is a simple way of finding the maximum
# of a function.

print(np.max(y))

# Use logical indexing or otherwise to find the value of t at which y is maximal. Does
# this match up with what you see in your plot?

idx = y == np.max(y)
print(t[idx])


