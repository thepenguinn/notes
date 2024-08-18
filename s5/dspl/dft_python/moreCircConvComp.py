import matplotlib.pyplot as plt
import numpy as np

def circonv(g, h):

    if g.size > h.size:
        h = np.concatenate([h, np.zeros(g.size - h.size)])
    elif g.size < h.size:
        g = np.concatenate([g, np.zeros(h.size - g.size)])

    N = g.size
    htr = np.concatenate([[h[0]], h[:0:-1]])

    y = np.zeros(N)

    for n in np.arange(N):
        y[n] = np.sum(g * htr)
        htr = np.roll(htr, 1)

    return y, g, h

g = np.array([1, 2, 3, 4, 5])
h = np.array([2, 2, 0, 1, 1])

y, g, h = circonv(g, h)

plt.figure(figsize = (10, 13))

plt.subplot(3, 1, 1)
plt.stem(g, label = "g[n]")
plt.xlabel("n")
plt.ylabel("g[n]")
plt.legend()

plt.subplot(3, 1, 2)
plt.stem(h, label = "h[n]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.legend()

plt.subplot(3, 1, 3)
plt.stem(y, label = "$g[n] \circledcirc h[n]$")
plt.xlabel("n")
plt.ylabel("$y[n] = g[n] \circledcirc h[n]$")
plt.legend()


print("g[n] = ", end = "")
print(g)

print("h[n] = ", end = "")
print(h)

print("y[n] = ", end = "")
print(y)

plt.savefig("../dft_plots/moreCircConvComp.pdf")

