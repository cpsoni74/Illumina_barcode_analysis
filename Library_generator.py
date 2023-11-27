import csv

def generate_dna_sequences(length):
    bases = ['A', 'C', 'G', 'T']
    
    def generate_sequences_helper(current_sequence):
        if len(current_sequence) == length:
            return [current_sequence]
        
        sequences = []
        for base in bases:
            new_sequence = current_sequence + base
            sequences.extend(generate_sequences_helper(new_sequence))
        
        return sequences
    
    all_sequences = generate_sequences_helper("")
    return all_sequences

sequence_length = 10  # Change this to your desired sequence length
dna_sequences = generate_dna_sequences(sequence_length)

output_file = "dna_sequences.csv"
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    #csv_writer.writerow(["DNA Sequence"])
    
    for sequence in dna_sequences:
        csv_writer.writerow([sequence])

print(f"DNA sequences written to {output_file}")