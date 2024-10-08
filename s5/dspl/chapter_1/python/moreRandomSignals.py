import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0.0, np.sqrt(3), 75)

plt.stem(x)

plt.xlabel("Time")
plt.ylabel("Amplitude")

print("Mean of the random signal: " + str(np.mean(x)))
print("Variance of the random signal: " + str(np.var(x)))

plt.savefig("../plots/moreRandomSignals.pdf")

