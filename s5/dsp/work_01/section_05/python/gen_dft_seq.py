def gen_dft_seq(
    samp_count, samp_freq, real_freq, imag_freq
    ):

    cplx_fn = cplx_factory(
        samp_freq = samp_freq,
        real_freq = real_freq,
        imag_freq = imag_freq
    )

    cplx_seq = np.ndarray(samp_count, dtype = np.cdouble)

    for i in range(samp_count):
        cplx_seq[i] = cplx_fn(i)

    freq = np.arange(samp_count)

    dft_fn = dft_factory(cplx_seq = cplx_seq)
    dft_seq = dft_fn(freq)

    # we need to scale freq back
    return freq * samp_freq / samp_count, dft_seq, cplx_seq

