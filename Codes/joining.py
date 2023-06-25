file_names = ["corpus_output\corpus1.txt", "corpus_output\corpus2.txt", "corpus_output\corpus3.txt", "corpus_output\corpus4.txt", "corpus_output\corpus5.txt", "corpus_output\corpus6.txt", "corpus_output\corpus7.txt"]

# Output file name
output_file = "output.txt"

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over each file name
    for file_name in file_names:
        # Open each file in read mode
        with open(file_name, 'r') as infile:
            # Read the content of the file
            content = infile.read()
            # Write the content to the output file
            outfile.write(content)
            # Add a newline character after each file
            outfile.write('\n')
