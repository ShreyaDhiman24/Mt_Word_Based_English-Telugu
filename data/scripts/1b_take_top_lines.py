# def extract_lines(input_file, output_file, num_lines):
#     try:
#         with open(input_file, 'r') as infile:
#             lines = infile.readlines()
        
#         # Take only the first `num_lines` lines
#         lines_to_write = lines[:num_lines]
        
#         with open(output_file, 'w') as outfile:
#             outfile.writelines(lines_to_write)
        
#         print(f"Successfully extracted the first {num_lines} lines to '{output_file}'")
    
#     except FileNotFoundError:
#         print(f"Error: The file '{input_file}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Usage
# input_file = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/combined.txt'
# output_file = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/new_combined.txt'
# num_lines = 25000

# extract_lines(input_file, output_file, num_lines)

def take_top_lines(input_file_path, output_file_path, num_lines=15000):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    
    # Take the top `num_lines` lines
    top_lines = lines[:num_lines]
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in top_lines:
            output_file.write(line)

# Paths for the cleaned files
cleaned_en_path = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/cleaned_en.txt'
cleaned_te_path = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/cleaned_te.txt'

# Paths for the new files with top 15,000 lines
n_cleaned_en_path = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/n_cleaned_en.txt'
n_cleaned_te_path = '/home/shreya/Desktop/MajorProject/MT-Word_based/data/n_cleaned_te.txt'

# Take top 15,000 lines from cleaned_en.txt and cleaned_te.txt
take_top_lines(cleaned_en_path, n_cleaned_en_path, 25000)
take_top_lines(cleaned_te_path, n_cleaned_te_path, 25000)

print("Top 15,000 lines saved successfully to n_cleaned_en.txt and n_cleaned_te.txt")
