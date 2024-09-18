def gen_dtft_seq_64(
    cplx_seq, samp_freq, dtft_samp_count
    ):

    cplx_seq = np.concatenate(
        [cplx_seq, np.zeros(32, dtype = np.cdouble)]
    )

    freq = np.linspace(0, 1, dtft_samp_count)

    dtft_fn = dtft_factory(cplx_seq = cplx_seq)
    dtft_seq = dtft_fn(freq)

    # scaling back the freq from ($0$ - $1$) to ($0$ - $f_{s}$)
    return freq * samp_freq, dtft_seq, cplx_seq

