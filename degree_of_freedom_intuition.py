'''Why does degree of freedom reduction work for sample variance calculation?
-> So as to compensate for the reduction in variance, due to the population mean probabilistically not being equal to the sample mean '''

import numpy as np
import matplotlib.pyplot as plt

# Two samples from a population
x = np.array([180, 213])

# Function to return population variance
def fun(x,some_val):
    return np.sqrt((np.sum((x-some_val)**2))/(len(x)))

# x-axis values
i = np.array([a for a in np.arange(150,250,0.001)])

# y-axis values initialized to 0.0
y = np.array([0.0 for a in range(len(i))])

# y-axis values
for j in range(len(i)):
    y[j] = fun(x,i[j])

plt.plot(i,y)

# Line with equation x=196.5 (where 196.5 = (180+213)/2)
plt.plot([196.5 for a in np.arange(10,55,0.01)],[a for a in np.arange(10,55,0.01)],'red')

plt.show()
