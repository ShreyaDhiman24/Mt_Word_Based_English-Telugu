# Define input and output file paths
input_file = 'data/trainp.txt'
english_output_file = 'data/train_en.txt'
telugu_output_file = 'data/train_te.txt'

# Open the input file and output files
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(english_output_file, 'w', encoding='utf-8') as eng_outfile, \
     open(telugu_output_file, 'w', encoding='utf-8') as tel_outfile:

    # Read each line in the input file
    for line in infile:
        # Split the line by tab (\t) to separate English and Telugu parts
        parts = line.strip().split('\t')
        
        # Check if there are exactly 2 parts (English and Telugu)
        if len(parts) == 2:
            english_sentence, telugu_sentence = parts

            # Write the English sentence to the English output file
            eng_outfile.write(english_sentence + '\n')

            # Write the Telugu sentence to the Telugu output file
            tel_outfile.write(telugu_sentence + '\n')

print("Splitting completed successfully!")
