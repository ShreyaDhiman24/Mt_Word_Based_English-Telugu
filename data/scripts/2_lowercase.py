def lowercase_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    lowercased_lines = [line.lower() for line in lines]

    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(lowercased_lines)

# Example usage
input_file = 'data/z_cleaned_en.txt'
output_file = 'data/z_lowercase.txt'
lowercase_file(input_file, output_file)
