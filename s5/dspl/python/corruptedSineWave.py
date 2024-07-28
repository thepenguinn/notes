import numpy as np
import matplotlib.pyplot as plt

def corrupt_signal(sig, sdev):
    noise = np.random.normal(0, sdev, sig.size)
    return sig + noise

sdevs = [0.2, 0.7, 1.3]

t = np.arange(0, 2, 0.01)
signal = np.sin(2 * np.pi * t)

plt.figure(figsize = (10, 20))

plt.subplot(len(sdevs) + 1, 1, 1)
plt.plot(t, signal, label = "Original signal")
plt.legend()

for i in range(len(sdevs)):
    noisy_signal = corrupt_signal(signal, sdevs[i])
    plt.subplot(len(sdevs) + 1, 1, i + 2)
    plt.plot(
        t, noisy_signal,
        label = "Corrupted signal with gaussian noise of " + str(sdevs[i]) + " sdev"
    )
    plt.legend()

plt.savefig("plot/corruptedSineWave.pdf")