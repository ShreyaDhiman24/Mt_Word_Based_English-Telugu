import re

def count_sentences(text):
    # Consider sentences to end with '.', '!', or '?'.
    # Split text based on these delimiters.
    sentences = re.split(r'[.!?]', text)
    # Remove empty strings after split
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def filter_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            sentence_count = count_sentences(line)
            # Write the line to output file only if it has 60 or fewer sentences
            if sentence_count <= 60:
                outfile.write(line)

# Use the function on your dataset file
input_file = 'data/9_combined.txt'   # Replace with your actual input file name
output_file = 'data/10_combined.txt'  # Output file after filtering

filter_lines(input_file, output_file)
