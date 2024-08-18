import numpy as np

def circonv(g, h):

    if g.size != h.size:
        raise Exception("Sequences not of same length")

    N = g.size
    htr = np.concatenate([[h[0]], h[:0:-1]])

    y = np.zeros(N)

    for n in np.arange(N):
        y[n] = np.sum(g * htr)
        htr = np.roll(htr, 1)

    return y


