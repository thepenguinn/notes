import matplotlib.pyplot as plt
import numpy as np

global np

N = 4

def dft_func (k, n):
    global N
    return np.exp(-1j * 2 * np.pi / N * k * n)

D = np.empty((N, N), dtype = np.cdouble)

for k in range(N):
    for n in range(N):
        D[k, n] = dft_func(k, n)

np.round(D)

print(D)

