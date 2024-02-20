import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(-100, 100)

ypoints = 3*xpoints*xpoints-5

plt.plot(xpoints, ypoints)
plt.grid()
plt.show()
