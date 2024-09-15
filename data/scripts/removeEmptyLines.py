import re

def is_english(s):
    # Checks if the string contains any English alphabet characters
    return bool(re.search(r'[A-Za-z]', s))

def is_telugu(s):
    # Checks if the string contains any Telugu characters (Unicode range)
    return bool(re.search(r'[\u0C00-\u0C7F]', s))

def filter_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Split the line by tab
            parts = line.strip().split('\t')
            if len(parts) == 2:  # Ensure there are two parts after splitting
                eng_part, telugu_part = parts[0], parts[1]
                
                # Check if the first part is English and the second part is Telugu
                if is_english(eng_part) and is_telugu(telugu_part):
                    outfile.write(line)
                # Check if the first part is Telugu and the second part is English
                elif is_telugu(eng_part) and is_english(telugu_part):
                    outfile.write(line)

# Usage
input_file = 'data/11_combined.txt'
output_file = 'data/11a_combined.txt'
filter_lines(input_file, output_file)
