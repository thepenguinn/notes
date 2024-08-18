import numpy as np
import matplotlib.pyplot as plt

def comp_exp_func (n):
    return np.exp( (-1 / 12) + (1j * np.pi / 6 * n) )

t = np.arange(0, 41)
x = comp_exp_func(t)

plt.figure(figsize = (10, 16))

plt.subplot(2, 1, 1)
plt.stem(t, x.real, label = "Real part")
plt.legend()

plt.subplot(2, 1, 2)
plt.stem(t, x.imag, label = "Imaginary part")
plt.legend()

plt.savefig("../plot/complexExpSeq.pdf")