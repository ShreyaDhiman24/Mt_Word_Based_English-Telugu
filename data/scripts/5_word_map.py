from collections import defaultdict
import re

def preprocess_text(text):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def create_word_map(input_file, output_file):
    word_map = defaultdict(int)
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            # Preprocess the line to remove punctuation and lowercase the text
            cleaned_line = preprocess_text(line)
            words = cleaned_line.split()
            
            # Update word frequencies in the word map
            for word in words:
                word_map[word] += 1
    
    # Write the word map to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word, count in sorted(word_map.items()):
            outfile.write(f'{word}: {count}\n')

# Use the function on your dataset file
input_file = 'data/10_combined.txt'  # Replace with your actual input file name
output_file = 'data/10a_word_map.txt'  # Output file for the word map

create_word_map(input_file, output_file)

