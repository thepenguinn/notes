import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2 * np.pi, 2 * np.pi, 300)
x = np.sin(t)

plt.figure(figsize = (6, 11))

values = np.arange(- 2 * np.pi, 2.5 * np.pi, np.pi / 2)

labels = [
    "$- 2 \\pi$", "$- \\dfrac{3 \\pi}{2}$", "$- \\pi$", "$- \\dfrac{\\pi}{2}$",
    "$0$",
    "$\\dfrac{\\pi}{2}$", "$\\pi$", "$\\dfrac{3 \\pi}{2}$", "$2 \\pi$"
]

plt.subplot(2, 1, 1)
plt.plot(t, x)

plt.title("Sine Wave")
plt.xticks(values, labels)

plt.xlabel("t")
plt.ylabel("$\\sin (t)$")

plt.subplot(2, 1, 2)
plt.plot(t, abs(x))

plt.title("Full Rectified Sine Wave")
plt.xticks(values, labels)

plt.xlabel("t")
plt.ylabel("$x(t)$")

plt.savefig("../plot/rectifiedSine.pdf")
