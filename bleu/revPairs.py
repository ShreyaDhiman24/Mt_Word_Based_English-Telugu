# Script to reverse Telugu-English pairs in a file

# Define input and output file paths
input_file = 'bleu/output_for_appending.txt'
output_file = 'bleu/REVoutput_for_appending.txt'

# Open the input file for reading and output file for writing
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Split the line at the tab to separate Telugu and English
        pair = line.strip().split('   ')
        if len(pair) == 2:
            # Reverse the pair (English first, then Telugu) and write to output file
            outfile.write(f"{pair[1]}\t{pair[0]}\n")

print("File processing complete. Reversed pairs saved to", output_file)
