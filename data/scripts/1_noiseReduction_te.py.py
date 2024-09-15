import re

def clean_telugu_text(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = []
    for line in lines:
        # Remove non-Telugu characters and numbers
        line = re.sub(r'[^\u0C00-\u0C7F\s]', '', line)
        # Remove extra punctuation (keeping only valid sentence structure)
        line = re.sub(r'[.!?]', '', line)
        cleaned_lines.append(line.strip())
    
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            if line:  # Avoid writing empty lines
                file.write(line + '\n')

# Example usage
input_file = 'data/te.txt'
output_file = 'data/z_cleaned_te.txt'
clean_telugu_text(input_file, output_file)
