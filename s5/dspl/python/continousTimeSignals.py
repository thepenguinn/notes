import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.02)
x = np.sin(2 * np.pi * 1 * t)
y = np.sin(2 * np.pi * 2 * t)

plt.plot(t, x, label = "1 Hz")
plt.plot(t, y, label = "2 Hz")
plt.legend()

plt.savefig("../plot/continousTimeSignals.pdf")