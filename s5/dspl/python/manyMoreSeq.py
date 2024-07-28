import numpy as np
import matplotlib.pyplot as plt

def func_a (n):
    return 20 * (0.9 ** n)

def func_b (n):
    return 0.2 * (1.2 ** n)

def func_c (n):
    return (-0.8 ** n)

def func_d (n):
    return -4 * (0.8 ** n)

def func_e (n):
    return 2 * n * (0.9 ** n)

t = np.arange(0, 51)
a = func_a(t)
b = func_b(t)
c = func_c(t)
d = func_d(t)
e = func_e(t)

plt.figure(figsize = (10, 20))

plt.subplot(5, 1, 1)
plt.stem(t, a)

plt.subplot(5, 1, 2)
plt.stem(t, b)

plt.subplot(5, 1, 3)
plt.stem(t, c)

plt.subplot(5, 1, 4)
plt.stem(t, d)

plt.subplot(5, 1, 5)
plt.stem(t, e)

plt.savefig("plot/manyMoreSeq.pdf")