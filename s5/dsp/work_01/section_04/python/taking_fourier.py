import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def ft_factory(x_fn, l_lim, u_lim):

    def gen_int_fn(xi):
        return lambda x: x_fn(x) * np.exp(-1j * 2 * np.pi * x * xi)

    def ft(xi):
        val = quad(gen_int_fn(xi), l_lim, u_lim, limlst = 1000)
        return val[0]

    return ft

def sin(t):
    return (np.sin(2 * np.pi * 3 * t) + np.cos(2 * np.pi * 2 * t) + np.sin(2 * np.pi * 10 * t)) # + 1j * np.sin(2 * np.pi * 4 * t)

freq = np.linspace(8, 20, 300)
ft = ft_factory(sin, 0, 4)

ft_val = np.ndarray(len(freq), dtype = np.cdouble)

# ft_val[0] = (1, 1j)
# print(ft_val[0])

for i in range(len(freq)):
    ft_val[i] = ft(freq[i])

# print(ft_val.real)

fn_val = sin(freq)

plt.subplot(3, 1, 1)
plt.plot(freq, fn_val)

plt.subplot(3, 1, 2)
plt.plot(freq, ft_val.real)

plt.subplot(3, 1, 3)
plt.plot(freq, ft_val.imag)

plt.savefig("../plots/ft.pdf")


