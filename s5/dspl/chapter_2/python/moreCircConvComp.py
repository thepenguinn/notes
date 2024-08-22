import matplotlib.pyplot as plt
import numpy as np

def circonv(g, h):

    if g.size > h.size:
        h = np.concatenate([h, np.zeros(g.size - h.size)])
    elif g.size < h.size:
        g = np.concatenate([g, np.zeros(h.size - g.size)])

    N = g.size
    htr = np.concatenate([[h[0]], h[:0:-1]])

    y = np.zeros(N)

    for n in np.arange(N):
        y[n] = np.sum(g * htr)
        htr = np.roll(htr, 1)

    return y, g, h

g = np.array([1, 2, 3, 4, 5])
h = np.array([2, 2, 0, 1, 1])

y, g, h = circonv(g, h)

print("g[n] = ", end = "")
print(g)

print("h[n] = ", end = "")
print(h)

print("y[n] = ", end = "")
print(y)


