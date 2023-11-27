import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logomaker

def make_base_matrix_columns(sequences):
    columns = set()
    for x in sequences:
        columns.update(set(x))
    return columns

def populate_logo_matrix(sequences, quantifications, columns=None):
    if columns is None:
        columns = make_base_matrix_columns(sequences)

    seq_len = len(sequences[0])
    ret = pd.DataFrame(np.zeros(shape=(seq_len, len(columns))),
                       index=list(range(seq_len)),
                       columns=columns)

    for s, q in zip(sequences, quantifications):
        if not np.isnan(q):
            for i, b in enumerate(s):
                ret.at[i, b] += q

    return ret

def make_logo_plot(fname, dat, width, height, font_size):
    seq_len = len(dat)
    x_labels = list(range(seq_len))

    #fig = plt.figure(figsize=[4,8])

    logo = logomaker.Logo(dat, color_scheme = 'colorblind_safe')
    logo.style_spines(visible=False)
    logo.style_xticks(visible=False)
    logo.ax.set_xticks(range(seq_len))
    logo.ax.set_xticklabels(x_labels)
    logo.ax.set_ylabel('Weighted Enrichment Factor')

   # Adjust the font size to change the size of the letters
    #plt.figure(figsize=(10,6))
    #plt.tight_layout()
    plt.gcf().set_size_inches(10, 12)
    plt.savefig(fname, format='png', dpi = 600)
    #plt.show()

hits_df = pd.read_csv('/Users/chintansoni/Desktop/MaPylRS paper_figures and data/Figure 1/DNA vs RNA Illumina/RNA_fractions_Ill.csv')
sequences = hits_df['barcode']
quantifications = hits_df['Fraction of total']
print (sequences)
print (quantifications)

col = make_base_matrix_columns(sequences)
df = populate_logo_matrix(sequences, quantifications, col)
#print(df)
df.to_csv('/Users/chintansoni/Desktop/MaPylRS paper_figures and data/Figure 1/DNA vs RNA Illumina/RNA_base_fractions_Ill.csv')

make_logo_plot('/Users/chintansoni/Desktop/MaPylRS paper_figures and data/Figure 1/DNA vs RNA Illumina/RNA_weblogo.png', df, 60, 80, 12)


