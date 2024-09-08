import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (6, 2.5))

def dtft_factory(x_signal):

    length = len(x_signal)
    def dtft(freq):
        sum = 0
        for n in range(len(x_signal)):
            sum = sum + x_signal[n] * np.exp(-1j * 2 * np.pi * freq * n / length)

        return sum

    return dtft

def sin_factory(freq):
    return lambda t: np.cos(2 * np.pi * freq * t)

time = np.linspace(0, 1, 30)
sin = sin_factory(1)
sin_val = sin(time)

sin_dtft = dtft_factory(sin_val)

# plt.stem(time, sin_val)
# plt.savefig("../plots/test.pdf")

freq = np.linspace(0, 30, 30 * 30)

freq_val = sin_dtft(freq)

plt.stem(freq, freq_val)
plt.savefig("../plots/test.pdf")


