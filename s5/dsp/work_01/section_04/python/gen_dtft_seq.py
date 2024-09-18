def gen_dtft_seq(
    samp_count, samp_freq, real_freq, imag_freq, dtft_samp_count
    ):

    cplx_fn = cplx_factory(
        samp_freq = samp_freq,
        real_freq = real_freq,
        imag_freq = imag_freq
    )

    cplx_seq = np.ndarray(samp_count, dtype = np.cdouble)

    for i in range(samp_count):
        cplx_seq[i] = cplx_fn(i)

    freq = np.linspace(0, 1, dtft_samp_count)

    dtft_fn = dtft_factory(cplx_seq = cplx_seq)
    dtft_seq = dtft_fn(freq)

    # scaling back the freq from ($0$ - $1$) to ($0$ - $f_{s}$)
    return freq * samp_freq, dtft_seq, cplx_seq

