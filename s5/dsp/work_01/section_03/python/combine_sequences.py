import numpy as np
import pandas as pd

X = 28
t = np.linspace(0, np.pi / 4, 2500)

x1 = np.sin( 2 * np.pi * X * t)
x2 = np.sin( 2 * np.pi * (2 * X) * t)
x3 = np.sin( 2 * np.pi * ((2 * X) + 0.1) * t)

real = [x1, x2, x3]
imag = [x1, x2, x3]

pd.DataFrame( {
    "x1": x1[0:625],
    "x2": x2[0:625],
    "x3": x3[0:625],
}).to_csv(
    "../data/short_sequences.csv",
    sep = " ", index_label = "time"
)

cplx_labels = [
    "complex_a",
    "complex_b",
    "complex_c",
    "complex_d",
    "complex_e",
    "complex_f",
    "complex_g",
    "complex_h",
    "complex_i",
]

cplx = []

for r in real:
    for i in imag:
        cplx.append(pd.DataFrame({
            "real": r,
            "imag": i,
        }))

for i in range(len(cplx)):
    cplx[i].to_csv(
        "../data/" + cplx_labels[i] + ".csv",
        sep = " ", index_label = "time"
    )


