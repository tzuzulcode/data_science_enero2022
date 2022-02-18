import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

plt.style.use('classic')

x = np.linspace(-10,10,101)


plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))

plt.show()