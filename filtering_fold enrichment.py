import csv

# Input and output CSV file paths
input_csv_path = '/Users/chintansoni/Desktop/MaPyl Barcoding library seq/10Nx MaPylRS analysis/Data Analysis/NNK_noUaa/09-06-23_no Uaa fold enrichment.csv'
output_csv_path = '/Users/chintansoni/Desktop/MaPyl Barcoding library seq/10Nx MaPylRS analysis/Data Analysis/NNK_noUaa/09-06-23_no Uaa fold enrichment_filtered.csv'

# Open input and output CSV files
with open(input_csv_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Write the header row to the output CSV
    header = next(csv_reader)
    csv_writer.writerow(header)

    # Loop through each row in the input CSV
    for row in csv_reader:
        # Assuming out1 and out2 are in the second and third columns (index 1 and 2)
        out1_str = row[1]
        out2_str = row[2]

        # Check if either out1 or out2 is empty or non-numeric
        if out1_str and out2_str:
            try:
                out1 = float(out1_str)
                out2 = float(out2_str)

                # Check if either out1 or out2 is greater than or equal to 10
                if out1 >= 5 and out2 >= 5:
                    # If both out1 and out2 are greater than or equal to 10, write the row to the output CSV
                    csv_writer.writerow(row)
            except ValueError:
                # Handle the case where the values cannot be converted to floats
                print(f"Skipping row {row} due to non-numeric values.")

print("Filtered CSV created successfully.")