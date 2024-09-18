import numpy as np

def dft_factory(cplx_seq):

    sample_count = len(cplx_seq)
    def dft(k):
        sum = 0
        # see eq. ($\ref{eqn:dftK}$)
        for n, cplx in enumerate(cplx_seq):
            sum = sum + cplx * np.exp(-1j * 2 * np.pi * k * n / sample_count)
        return sum

    return dft

