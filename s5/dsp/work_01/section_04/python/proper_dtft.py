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

# 0 * (1 / samp_freq)
def disc_seq(samp_freq, freq):
    samp_period = 1 / samp_freq
    return lambda n: np.cos(2 * np.pi * freq * samp_period * n)

# i dont get this, shit im an idiot
seq = disc_seq(500, 30)
seq_val = []
for i in range(64):
    seq_val.append(seq(i))

seq_val = np.array(seq_val)

dtft = dtft_factory(seq_val)

freq = np.linspace(0, 30, 31)

dtft_val = dtft(freq)

plt.stem(freq, dtft_val.real)
plt.savefig("../plots/proper_dtft.pdf")


