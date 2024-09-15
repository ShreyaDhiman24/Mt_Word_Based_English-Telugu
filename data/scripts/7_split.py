import os

# Define file paths
combined_file_path = 'data/11_combined.txt'
train_file_path = 'data/trainp.txt'
test_file_path = 'data/testp.txt'
dev_file_path = 'data/devp.txt'

# Read the combined file
with open(combined_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Calculate split indices
total_lines = len(lines)
train_end = int(0.75 * total_lines)  # 75% for training
test_end = train_end + int(0.15 * total_lines)  # 15% for testing

# Split lines into train, test, and dev
train_lines = lines[:train_end]
test_lines = lines[train_end:test_end]
dev_lines = lines[test_end:]

# Write to train file
with open(train_file_path, 'w', encoding='utf-8') as file:
    file.writelines(train_lines)

# Write to test file
with open(test_file_path, 'w', encoding='utf-8') as file:
    file.writelines(test_lines)

# Write to dev file
with open(dev_file_path, 'w', encoding='utf-8') as file:
    file.writelines(dev_lines)

print("Dataset split into train, test, and dev files successfully.")
print(f"Training file created at: {train_file_path}")
print(f"Testing file created at: {test_file_path}")
print(f"Development file created at: {dev_file_path}")
