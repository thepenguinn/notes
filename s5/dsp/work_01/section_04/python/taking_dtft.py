import numpy as np
import matplotlib.pyplot as plt

# F = 28
# t = np.linspace(0, np.pi / 16, 1000)
#
# x1 = np.sin( 2 * np.pi * F * t)
# x2 = np.sin( 2 * np.pi * (F + 0.1) * t)
# x3 = np.sin( 2 * np.pi * 2 * F * t)
#
# cplx_a = x1 + 1j * x1
# cplx_b = x1 + 1j * x2
# cplx_c = x1 + 1j * x3
# cplx_f = x2 + 1j * x3

def dtft_factory(x_signal):

    def dtft(omega):
        sum = 0
        for n in range(len(x_signal)):
            sum = sum + x_signal[n] * np.exp(-1j * omega * n)

        return sum

    return  dtft

## dtft = dtft_factory(cplx_a[0:10])
# dtft = dtft_factory(np.array([0, 1, 2, 3, 4, 4, 4, 4, 3, 2, 1, 0], dtype = np.cdouble))
time = np.linspace(0, 1, 1000)
sin = np.sin(2 * np.pi * 3 * time) + np.sin(2 * np.pi * 1 * time)

plt.subplot(3, 1, 1)
plt.plot(time, sin)
plt.grid()

dtft = dtft_factory(sin)
freq = np.linspace(0, 1, 1000)
out = dtft(freq)

plt.subplot(3, 1, 2)
plt.plot(freq, out.real)
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(freq, out.imag)
plt.grid()

plt.savefig("../plots/test.pdf")
# print(cplx_a)



# A = fft.fft(cplx_a)

# plt.subplot(2, 1, 1)
# plt.plot(t, A.real)
# plt.grid()
#
# plt.subplot(2, 1, 2)
# plt.plot(t, A.imag)
#
# plt.savefig("../plots/test.pdf")
#
# print(numpy)


