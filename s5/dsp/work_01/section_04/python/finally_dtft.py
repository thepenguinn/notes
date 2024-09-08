import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (6, 2.5))

def dtft_factory(x_signal):

    def dtft(freq):

        sum = 0
        for n in range(len(x_signal)):
            sum = sum + x_signal[n] * np.exp(-1j * 2 * np.pi * n * freq)

        return sum

    return dtft

def sin_factory(freq):
    return lambda t: np.cos(2 * np.pi * freq * t) + 1j * np.cos(2 * np.pi * 10 * freq * t)

N = 1000

time = np.linspace(0, 1, N)
sin = sin_factory(4)
sin_val = sin(time)

dtft = dtft_factory(sin_val)

freq = np.linspace(0, 1, 1000)

final = np.ndarray(len(freq), dtype = np.cdouble)

for i, f in enumerate(freq):

    final[i] = dtft(f)
    # print(final[i])
    if final[i].real > 10:
        print("Real", f * N)
    if final[i].imag > 10:
        print("Imaginary", f * N)

# plt.plot(freq * N, final.imag)
# plt.savefig("../plots/imdying.pdf")

