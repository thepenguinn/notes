import numpy as np
import matplotlib.pyplot as plt

a = np.arange(6)
b = np.arange(4, -1, -1)

x = np.concatenate([a, b])

plt.stem(x)
plt.xticks(np.arange(11))

plt.savefig("plot/discreteTimeTri.pdf")