import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)
x = n.copy()

plt.stem(n, x)

plt.xlabel("$n$")
plt.ylabel("$x[n]$")

plt.xticks(n)

plt.savefig("../plot/discreteTimeRamp.pdf")