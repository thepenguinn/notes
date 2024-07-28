import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2 * np.pi, 2 * np.pi, 0.02)
s = np.sin(t)
rs = np.abs(s)

plt.plot(t, s, label = "Non Rectified")
plt.plot(t, rs, label = "Rectified")
plt.legend()

plt.savefig("../plot/rectifiedSine.pdf")