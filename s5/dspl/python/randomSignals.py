import numpy as np
import matplotlib.pyplot as plt

x = np.random.random_sample(100)
x = (x * 4) - 2

plt.stem(x)

plt.savefig("../plot/randomSignals.pdf")