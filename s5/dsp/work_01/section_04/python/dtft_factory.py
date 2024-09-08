import numpy as np

def dtft_factory(cplx_seq):

    def dtft(freq):
        sum = 0
        # see Equation $\ref{eqn:dtftFreq}$
        for n, cplx in enumerate(cplx_seq):
            sum = sum + cplx * np.exp(-1j * 2 * np.pi * freq * n)
        return sum

    return dtft

seq = np.array([1, 1, 1, 1])
dtft = dtft_factory(seq)

print(type(dtft), end = "\n\n")

print(dtft(0))
print(dtft(1))
# $\mbox{\textsc{Z Transform}}$


