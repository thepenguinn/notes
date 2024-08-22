import numpy as np
import matplotlib.pyplot as plt

N = 64
D = np.empty((N, N), dtype = np.cdouble)

W = np.exp(-1j * 2 * np.pi / N)
k = np.arange(N)

for n in np.arange(N):
    D[:, n] = W ** (k * n)

np.round(D)
plt.imshow(D.real)
plt.savefig("../plots/dftMatrixSixtyFourPointReal.pdf", bbox_inches = "tight")

plt.clf()
plt.imshow(D.imag)
plt.savefig("../plots/dftMatrixSixtyFourPointImaginary.pdf", bbox_inches = "tight")

