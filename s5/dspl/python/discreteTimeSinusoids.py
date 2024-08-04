import numpy as np
import matplotlib.pyplot as plt

def func_a (n):
    return np.sin(0.2 * np.pi * n)

def func_b (n):
    return np.sin(1.8 * np.pi * n)

def func_c (n):
    return np.sin(2.2 * np.pi * n)

t = np.arange(0, 51)
a = func_a(t)
b = func_b(t)
c = func_c(t)

plt.figure(figsize = (10, 20))

plt.subplot(3, 1, 1)
plt.stem(t, a)

plt.xlabel("$n$")
plt.ylabel("$x_{1}[n] = \\sin(0.2 \\pi n)$")

plt.subplot(3, 1, 2)
plt.stem(t, b)

plt.xlabel("$n$")
plt.ylabel("$x_{2}[n] = \\sin(1.8 \\pi n)$")

plt.subplot(3, 1, 3)
plt.stem(t, c)

plt.xlabel("$n$")
plt.ylabel("$x_{3}[n] = \\sin(2.2 \\pi n)$")

plt.savefig("../plot/discreteTimeSinusoids.pdf")