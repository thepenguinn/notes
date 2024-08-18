import numpy as np
from scipy.linalg import circulant

def circonv(g, h):

    if g.size > h.size:
        h = np.concatenate([h, np.zeros(g.size - h.size)])
    elif g.size < h.size:
        g = np.concatenate([g, np.zeros(h.size - g.size)])

    N = g.size
    htr = np.concatenate([[h[0]], h[:0:-1]], dtype = np.cdouble)

    y = np.zeros(N, dtype = np.cdouble)

    for n in np.arange(N):
        y[n] = np.sum(g * htr)
        htr = np.roll(htr, 1)

    return y, g, h

g = np.array([1, 2, 3, 4, 5], dtype = np.cdouble)
h = np.array([2, 2, 0, 1, 1], dtype = np.cdouble)

y, g, h = circonv(g, h)

circ_mat = circulant(h)

my = circ_mat @ g

print("Circulant matrix of h[n]:")
print(circ_mat)

print("")

print("Convolution obtained through performing circular convolution:" )
print(y)

print("")

print("Convolution obtained through matrix method:" )
print(my)

