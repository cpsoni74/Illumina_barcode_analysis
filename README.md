# Illumina_barcode_analysis
#This code is to analyse the tRNA sequences by NGS

**#Modifying the fastq files**

1) First, edit the fastq files to eliminate diverisity sequences at 5' and 3' end of the tRNA. The tRNA extension from polymerase has 15Ts. Only 10Ts were accounted for the Illumina to avoid errors in the homopolymeric region and increase the confidence. 

2) The code read_length.fastq was used to modify the selection input and output files. The modified files were moved to the NGS folder (location can be modified in the parameters file). Make sure to label input and output files: in_mod_selection, out1_mod_selection, out2_mod_selection and so on. 

3) Input files are no oxidation or no selection condition, while output files are either + ncAA or -ncAA + oxidation/selection conditions.

**#Generating all possible library sequences**

1) Use Library_generator.py to generate all possible sequences for the randomized region. The sequence length can be set in the .py file. 

**#Modifying the parameters file**

1) The parameters file was edited to enter the name of the project, location of the working folder, library sequence file (one generated using library_generator.py). 

2) Include a reference sequence (make sure the sequence matches with the modification you have made to the fastq files)

3) Input constant base regions and randomized regions based on the modified file.

4) You can set Qscore threshold for each region, Q1 and Q2. For these analyses, Q1 was set to 10 and Q2 to 30.

5) Number of mismatches is predicted based on the Qscore threshold. It is generally rounded up to the next integer value.

6) Set minimum library count to 1 and enter the sequence format for output_format and full_seq_format: In this case, 10Ns => NNNNNNNNNN

7) Make sure to save the parameters file as a .csv file.

**#Running the code**

1) Run the Main.py file. It will generate a csv file with raw counts of each sequence detected in input file. 

**#Calculating enrichment**

1) Calculate the total number of raw counts for each selection condition (input & output). Calculate fraction of total for each barcode based on the total count in that condition.

2) Enrichment is calculated as follows: (fraction of total output)/(fraction of total input)

3) Average enrichment is average for each barcode across the duplicate selections. 

**#Filtering barcodes based on long-read sequencing of input library**

1) Use common_barcodes.py to generate the file.

2) Enter the path to file1 and file2 and the output file. Run the code to generate the file with barcodes present in the long-read sequencing. 

**#Merging +ncAA and -ncAA**

1) The above procedure needs to be followed for both +ncAA and -ncAA separately. 

2) Label average enrichment as average_ncAA and average_noncAA respectively. 

3) Now, both +ncAA and -ncAA files are merged using the common_barcodes.py file as described previously. 

**#Filtering barcodes based on enrichment factor**

Now, we filter barcodes such that the average fold enrichment +ncAA > 2 and average fold enrichment +ncAA/-ncAA > 2 using n_fold_enrichment + - ncAA.py




