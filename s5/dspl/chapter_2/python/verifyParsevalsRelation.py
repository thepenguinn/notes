import numpy as np
from scipy import fft

N = 500

g = np.random.random_sample(N) + 1j * np.random.random_sample(N)

LHS = np.sum(np.abs(g) ** 2)

G = fft.fft(g)

RHS = 1 / G.size * np.sum(np.abs(G) ** 2)

print("LHS:")
print(LHS)

print("")

print("RHS:")
print(RHS)

