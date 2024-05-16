"""
Gradient descent using the equation y = x^3 - 5x

200 iterations - each time uses the slope of y = x^3 - 5x to calculate the next x-value. 
Depending on the starting x-value it will either reach the local minimum or negative infinity.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

# initializing basic algorithm variables
eta = 0.05 # learning rate
x = -1.25 # starting value of x
x_values = [] # empty list to store future values of x

# iterating 200 times and using the slope and eta each 
# time to find the next x-value that is farther down the slope
for i in range(200):
    x = x - eta*(3*x**2-5)
    x_values.append(x)

# calculating y-values for each graph based on the equation and the x-values
y_values = np.array(x_values)**3 - np.array(x_values)*5 # y-values of the x-values that were found by the algo
x=np.arange(-3.5,3.5,0.01) # set of x-values for the equation graph
y = x**3 - 5*x # set of y-values for the equation graph


# makes a graph of the x-values
plt.plot(x_values)

# graph of equation and scatter plot of values found by the algo
plt.figure()
plt.plot(x,y)
plt.scatter(x_values,y_values)
plt.axis("equal")
plt.grid()