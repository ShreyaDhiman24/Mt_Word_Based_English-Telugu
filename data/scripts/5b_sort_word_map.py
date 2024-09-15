def sort_word_map(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Split lines into tuples of word and frequency, and convert frequency to integer
    word_freq = [(line.split(': ')[0], int(line.split(': ')[1])) for line in lines]

    # Sort the list by frequency in descending order
    sorted_word_freq = sorted(word_freq, key=lambda x: x[1], reverse=True)

    # Write the sorted data back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, freq in sorted_word_freq:
            file.write(f"{word}: {freq}\n")

# Replace 'path_to_your_file.txt' with the actual path to your word_map.txt file
file_path = 'data/10a_word_map.txt'
sort_word_map(file_path)
