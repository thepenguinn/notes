import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

t = np.linspace(0, 6, 500)

def fgen(fn, a, b):
    def fs(s):
        return quad(lambda t: fn(t) * np.exp(-1j * 2 * np.pi * s * t), a, b)

    return fs

def sin(t):
    return np.cos(2 * np.pi * t) + np.cos(2 * np.pi * 3 * t) + np.sin(2 * np.pi * 5 * t)

fs = fgen(sin, 0, 2 * np.pi)

# print(xt)
# print(fs(0))

seq = np.array([fs(v) for v in t])

## print(seq)
# plt.plot(seq.real)
plt.plot(t, sin(t))
# plt.plot(t, seq.real)

plt.savefig("../plots/test.pdf")

## print(quad(fn, 0, 1))


