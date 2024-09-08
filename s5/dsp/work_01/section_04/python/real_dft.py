import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

plt.figure(figsize = (6, 2.5))

def dft_factory(x_signal):
    length = len(x_signal)

    def dft(k):
        sum = 0

        for n, xn in enumerate(x_signal):
            sum = sum + xn * np.exp(-1j * 2 * np.pi * k * n / length)

        return sum

    return dft

def sin_factory(freq):
    return lambda t: np.cos(2 * np.pi * freq * t)

N = 500

time = np.linspace(0, 1, N)
sin = sin_factory(8)
sin_val = sin(time)

dft = dft_factory(sin_val)

dft_val = []
for i in range(N):
    dft_val.append(dft(i))
    if dft_val[i] > 4:
        print(i)


plt.stem(dft_val)
plt.savefig("../plots/delme.pdf")


