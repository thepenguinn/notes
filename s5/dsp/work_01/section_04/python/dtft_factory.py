import numpy as np

def dtft_factory(cplx_seq):

    def dtft(freq):
        sum = 0
        # see eq. ($\ref{eqn:dtftFreq}$)
        for n, cplx in enumerate(cplx_seq):
            sum = sum + cplx * np.exp(-1j * 2 * np.pi * freq * n)
        return sum

    return dtft

