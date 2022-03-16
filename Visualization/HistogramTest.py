import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-white")

data = np.random.randn(1000)
plt.hist(data,bins=30,label="Data",rwidth=0.5,align="mid",range=(-4,4),density=True,alpha=0.5,histtype="barstacked",color="red",edgecolor="none")
plt.show()