import nltk
from nltk.corpus import stopwords

# Load the English file
with open('/home/shreya/Desktop/MajorProject/1_ENG_TEL_MT-Word_based/data/2_lowercase.txt', 'r') as f:
    text = f.read()

# Split the text into words
words = text.split()

# Load the English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Join the filtered words back into a string
filtered_text = ' '.join(filtered_words)

print(filtered_text)