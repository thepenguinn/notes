for cplx in cplx_seqs:
    for seq_name in cplx["sequences"]:
        freq, dft_seq, _ = gen_dft_seq_64(
            cplx_seq = cplx["sequences"][seq_name],
            samp_freq = samp_freqs[seq_name]
        )

        data = pd.DataFrame(
            data = {
                "real": dft_seq.real,
                "imag": dft_seq.imag,
            },
            index = freq
        )

        data.to_csv(
            "../data/dft_" + cplx["name"] + "_" + seq_name + "_64.csv",
            sep = " ", index_label = "freq"
        )

