import pandas as pd

X = 28

cplx_seqs = [
    {
        "name": "complex_a",
        "real_freq": X,
        "imag_freq": X,
        # we will fill this later, for taking 64 point DTFT
        "sequences": {},
    },
    {
        "name": "complex_b",
        "real_freq": X,
        "imag_freq": 2 * X,
        "sequences": {},
    },
    {
        "name": "complex_c",
        "real_freq": X,
        "imag_freq": (2 * X) + 0.1,
        "sequences": {},
    },
    {
        "name": "complex_f",
        "real_freq": 2 * X,
        "imag_freq": (2 * X) + 0.1,
        "sequences": {},
    },
]

samp_freqs = {
    "normal":           int(4 * X),
    "slightly_greater": int(4 * X + 10),
    "much_greater":     int(4 * X * 6),
    "much_lesser":      int(4 * X / 2),
}

samp_count = 32

dtft_samp_count = 2000

for cplx in cplx_seqs:

    for samp_freq in samp_freqs:

        freq, dtft_seq, cplx_seq = gen_dtft_seq(
            samp_count = samp_count,
            samp_freq = samp_freqs[samp_freq],
            real_freq = cplx["real_freq"],
            imag_freq = cplx["imag_freq"],
            dtft_samp_count = dtft_samp_count
        )

        # keeping generated sequences for taking 64 point DTFT
        cplx["sequences"][samp_freq] = cplx_seq

        data = pd.DataFrame(
            data = {
                "real": dtft_seq.real,
                "imag": dtft_seq.imag,
            },
            index = freq
        )

        data.to_csv(
            "../data/dtft_" + cplx["name"] + "_" + samp_freq + "_32.csv",
            sep = " ", index_label = "freq"
        )

