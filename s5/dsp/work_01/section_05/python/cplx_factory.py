def cplx_factory(samp_freq, real_freq, imag_freq):
    samp_period = 1 / samp_freq
    return lambda n: np.sin(
        2 * np.pi * real_freq * (n * samp_period)
    ) + 1j * np.sin(
        2 * np.pi * imag_freq * (n * samp_period)
    )

