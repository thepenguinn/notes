import numpy as np
from scipy import fft

g = np.concatenate([np.arange(128), np.arange(128, -1, -1)])

LHS = np.sum(g ** 2)

G = fft.fft(g)

RHS = 1 / G.size * np.sum(np.abs(G) ** 2)

print("LHS:")
print(LHS)

print("")

print("RHS:")
print(RHS)

