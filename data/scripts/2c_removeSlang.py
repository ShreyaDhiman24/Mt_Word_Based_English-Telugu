# Load the English file
with open('/home/shreya/Desktop/MajorProject/1_ENG_TEL_MT-Word_based/data/2_lowercase.txt', 'r') as f:
    text = f.read()

# Split the text into words
words = text.split()

# Define a list of slang/acronyms words to remove
slang_words = ['lol', 'brb', 'btw', ...]  # add more words as needed

# Remove slang/acronyms words
filtered_words = [word for word in words if word not in slang_words]

# Join the filtered words back into a string
filtered_text = ' '.join(filtered_words)

print(filtered_text)