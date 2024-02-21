import matplotlib.pyplot as plt
import numpy as np

range = float(input("Range: "))

x = np.linspace(-range, range)

eq = input("Function: ")

y = eval(eq)

plt.plot(x, y)
plt.grid()
plt.show()
