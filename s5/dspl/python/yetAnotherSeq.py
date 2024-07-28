import numpy as np
import matplotlib.pyplot as plt

def yet_another_func(n):
    return (0.95 ** n) * np.cos(0.1 * np.pi * n)

t = np.arange(0, 51)
x = yet_another_func(t)

plt.stem(t, x)

plt.savefig("plot/yetAnotherSeq.pdf")