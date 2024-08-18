import numpy as np
import matplotlib.pyplot as plt

N = 64
D = np.empty((N, N), dtype = np.cdouble)

W = np.exp(-1j * 2 * np.pi / N)
k = np.arange(N)

for n in np.arange(N):
    D[:, n] = W ** (k * n)

np.round(D)
real = plt.imshow(D.real)
real.set_cmap("gist_earth")
plt.savefig("../dft_plots/dftMatrixSixtyFourPointReal.pdf", bbox_inches = "tight")

plt.clf()
imag = plt.imshow(D.imag)
imag.set_cmap("gist_earth")
plt.savefig("../dft_plots/dftMatrixSixtyFourPointImaginary.pdf", bbox_inches = "tight")
# plt.imsave("../dft_plots/dftMatrixSixtyFourPointReal.pdf", D.real, dpi = 20)
# plt.imsave("../dft_plots/dftMatrixSixtyFourPointImaginary.pdf", D.imag, dpi = 20)

