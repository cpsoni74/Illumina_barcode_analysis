import pandas as pd

# Define the file paths
file1_path = '/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_BocK_ip.csv'
file2_path = '/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_noncAA_ip.csv'

# Read both CSV files into DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Drop duplicates from df2 based on the 'barcode' column
df2 = df2.drop_duplicates(subset='barcode')

# Find common barcodes between the two DataFrames
common_barcodes = set(df1['barcode']).intersection(set(df2['barcode']))

# Filter rows in df2 that have common barcodes
filtered_df2 = df2[df2['barcode'].isin(common_barcodes)]

# Merge data from df1 and filtered_df2 based on the 'barcode' column
merged_df = df1.merge(filtered_df2, on='barcode', how='inner')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('/Users/chintansoni/Desktop/NGS/11-1-23_10N + WT/Analysis/10N_BocK_noncAA_ip.csv', index=False)

print("Merged data saved successfully.")
