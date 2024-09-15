import re

def clean_english_text(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = []
    for line in lines:
        # Remove unnecessary numbers
        line = re.sub(r'\d+', '', line)
        # Remove unwanted punctuation
        line = re.sub(r'[^\w\s]', '', line)
        # Remove extra whitespace
        line = re.sub(r'\s+', ' ', line).strip()
        cleaned_lines.append(line)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            if line:  # Avoid writing empty lines
                file.write(line + '\n')

# Example usage
input_file = 'data/en.txt'
output_file = 'data/z_cleaned_en.txt'
clean_english_text(input_file, output_file)
