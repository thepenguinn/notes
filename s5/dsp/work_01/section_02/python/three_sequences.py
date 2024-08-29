import numpy as np
import pandas as pd

F = 28
t = np.linspace(0, 1.25 * np.pi / 4, 2500)

x1 = np.sin( 2 * np.pi * F * t)
x2 = np.sin( 2 * np.pi * (F + 0.1) * t)
x3 = np.sin( 2 * np.pi * 2 * F * t)

data = pd.DataFrame(
    {
        "x1": x1,
        "x2": x2,
        "x3": x3,
    }
)

data.to_csv(
    "../data/three_sequences.csv", sep = " ", index_label = "time"
)
print(data)


