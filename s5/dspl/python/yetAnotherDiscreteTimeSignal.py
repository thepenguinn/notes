import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, -1, 4, 1])

plt.xlabel("$n$")
plt.ylabel("$x[n]$")

plt.stem(x)

plt.savefig("../plot/yetAnotherDiscreteTimeSignal.pdf")