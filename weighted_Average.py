#weighted average of enrichment

import pandas as pd
import ast

# Load your data from a CSV file (replace 'your_data.csv' with your file's path)
file_path = '/Users/chintansoni/Desktop/average_BocK vs average no Uaa_2by2.csv'
data = pd.read_csv(file_path)


# Group the data by 'aaRS' and sum the 'average_Uaa' values
grouped_data = data.groupby('aaRS')['average_Uaa'].sum().reset_index()

# Display the result
print(grouped_data)

grouped_data.to_csv('/Users/chintansoni/Desktop/Top10%_NNK_BocK_sum.csv')
