def load_word_frequencies(word_map_path):
    word_freq = {}
    with open(word_map_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            word, freq = line.split(': ')
            word_freq[word.strip()] = int(freq.strip())
    return word_freq

def filter_sentences(input_file, word_freq, threshold, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    
    filtered_sentences = []
    for sentence in sentences:
        words = sentence.split()
        if not any(word in word_freq and word_freq[word] > threshold and len(word) >= 4 for word in words):
            filtered_sentences.append(sentence)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(filtered_sentences)

# Paths to your files
word_map_path = 'data/10a_word_map.txt'
input_file = 'data/10_combined.txt'
output_file = 'data/11_combined.txt'

# Load word frequencies
word_freq = load_word_frequencies(word_map_path)

# Filter sentences and write to a new file
filter_sentences(input_file, word_freq, 600, output_file)

print(f"Filtered sentences written to {output_file}")
