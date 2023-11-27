# at least 2-fold diff between +Uaa and -Uaa

import pandas as pd
import csv

df = pd.read_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_BocK_noncAA_average enrichment.csv')

filtered_df = df[df['average_noncAA'] <= (df['average_ncAA']/2)]

filtered_df.to_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_BocK_noncAA_atleast2.csv', index = False)

df2 = filtered_df[filtered_df['average_ncAA'] >= 2]

df2.to_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_BocK_noncAA_atleast2_min2.csv')
