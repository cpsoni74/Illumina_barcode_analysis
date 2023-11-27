# at least 3-fold diff between +Uaa and -Uaa

import pandas as pd
import csv

df = pd.read_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/+BocK WT/Results/10N_BocK_incrasing order av enrichment.csv')

#filtered_df = df[df['average_noUaa'] <= (df['average_Uaa']/2)]

#filtered_df.to_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/+BocK WT/Results/10N_BocK_non-zero.csv', index = False)

df2 = df[df['Average'] > 0]

df2.to_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/+BocK WT/Results/10N_BocK_nonzero.csv')
