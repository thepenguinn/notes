# fourier series

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapezoid

plt.clf()
plt.close()

plt.figure(figsize = (10, 4))

t = np.arange(0, 2, 0.01)

f = np.zeros_like(None, shape = 300)
f.fill(2)

g = np.zeros_like(t)
for i in range(len(t)):
    g[i] = t[i]

def stupid_conv (inc, ff, sf):

    # sf = np.flip(sf)
    conv = []

    if ff.size > sf.size:
        smallest_size = sf.size
        largest_size = ff.size
    else:
        smallest_size = ff.size
        largest_size = sf.size

    nt = np.arange(0, 3, inc)

    tmp = np.zeros_like(nt, dtype = "double")

    for i in range(smallest_size):
        tmp.fill(0)
        for j in range(i + 1):
            tmp[i - j] = np.minimum(sf[j], ff[i - j])
        conv.append(trapezoid(tmp, nt))

    if ff.size > sf.size:
        for i in range(ff.size - sf.size):
            tmp.fill(0)
            for j in range(sf.size):
                tmp[sf.size + i - j] = np.minimum(sf[j], ff[sf.size + i - j])
            conv.append(trapezoid(tmp, nt))
    elif ff.size < sf.size:
        pass

    # TODO: implement the rest

    return conv

conv = stupid_conv(0.01, f, g)
plt.plot(conv)
plt.plot(g)
# plt.plot(g)

# plt.xticks(np.arange(11))

plt.savefig("hai.pdf")
server.send(".".encode())
