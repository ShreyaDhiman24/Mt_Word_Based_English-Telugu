# File paths
input_file = "data/7_combinedFinal.txt"
output_file = "data/7_revPaircombinedFinal.txt"

# Open the input file and output file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    # Process each line
    for line in infile:
        # Split the line by tab to get English and Telugu sentences
        parts = line.strip().split('\t')
        if len(parts) == 2:
            # Reverse the pair: Telugu first, English second
            telugu_sentence = parts[1]
            english_sentence = parts[0]
            
            # Write the reversed pair to the output file
            outfile.write(f"{telugu_sentence}\t{english_sentence}\n")

print(f"Reversed translation pairs saved to {output_file}")
