def gen_dft_seq_64(
    cplx_seq, samp_freq
    ):

    cplx_seq = np.concatenate(
        [cplx_seq, np.zeros(32, dtype = np.cdouble)]
    )

    freq = np.arange(64)

    dft_fn = dft_factory(cplx_seq = cplx_seq)
    dft_seq = dft_fn(freq)

    # we need to scale freq back
    return freq * samp_freq / 64, dft_seq, cplx_seq

