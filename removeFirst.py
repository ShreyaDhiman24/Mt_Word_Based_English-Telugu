input_file = 'bleu/accepted_sentences.txt'  # Replace with your input file name
output_file = 'bleu/output_for_appending.txt'  # Replace with your desired output file name

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        parts = line.strip().split('   ')
        if len(parts) > 1:
            # Join the remaining parts (excluding the first one) with the delimiter '   '
            cleaned_line = '   '.join(parts[1:])
            outfile.write(cleaned_line + '\n')

