import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

N = 4
D = np.empty((N, N), dtype = np.cdouble)

W = np.exp(-1j * 2 * np.pi / N)
k = np.arange(N)

for n in np.arange(N):
    D[:, n] = W ** (k * n)

np.round(D)

x = np.array([[1, 2, 3, 4]]).T
X = D @ x

np.round(X)

print("DFT using matrix method:")
print(X)
print("")

# verifying using scipy.fft.fft()

SX = fft.fft(x, axis = 0)

print("DFT using scipy:")
print(SX)

