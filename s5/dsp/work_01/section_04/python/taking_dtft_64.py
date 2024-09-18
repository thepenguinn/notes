dtft_samp_count = 2000

for cplx in cplx_seqs:
    for seq_name in cplx["sequences"]:
        freq, dtft_seq, _ = gen_dtft_seq_64(
            cplx_seq = cplx["sequences"][seq_name],
            samp_freq = samp_freqs[seq_name],
            dtft_samp_count = dtft_samp_count
        )

        data = pd.DataFrame(
            data = {
                "real": dtft_seq.real,
                "imag": dtft_seq.imag,
            },
            index = freq
        )

        data.to_csv(
            "../data/dtft_" + cplx["name"] + "_" + seq_name + "_64.csv",
            sep = " ", index_label = "freq"
        )

