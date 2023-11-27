import pandas as pd

# Load the existing CSV file into a DataFrame
df = pd.read_csv('/Users/chintansoni/Desktop/MaPyl Barcoding library seq/10Nx MaPylRS analysis/Data Analysis/NST/NST_mIF_noUaa_atleast2min2_f.csv')

grouped_data = df.groupby('aaRS').agg({'barcode': list, 'average_Uaa': list}).reset_index()



# Group the data by 'aaRS' and count occurrences
aaRS_counts = df['aaRS'].value_counts().reset_index()

# Rename the columns for clarity
aaRS_counts.columns = ['aaRS', 'count']

# Save the grouped data to a new CSV file
grouped_data.to_csv('/Users/chintansoni/Desktop/NST_mIF_noUaa_2by2_f_grouped.csv', index=False)
aaRS_counts.to_csv('/Users/chintansoni/Desktop/NST_mIF_noUaa_2by2_f_counts.csv', index=False)