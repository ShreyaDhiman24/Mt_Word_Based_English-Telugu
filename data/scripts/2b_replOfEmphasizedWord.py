import re

# Load the English file
with open('/home/shreya/Desktop/MajorProject/1_ENG_TEL_MT-Word_based/data/2_lowercase.txt', 'r') as f:
    text = f.read()

# Define a dictionary to map emphasized words to their normal forms
emphasize_dict = {'coooooool': 'excellent', 'thaaaaaanks': 'thanks', 'ooooooooook': 'ok'}

# Use regular expressions to reduce repeated characters
text = re.sub(r'(.)\1{2,}', r'\1\1', text)

# Replace emphasized words with their normal forms
for emphasized, normal in emphasize_dict.items():
    text = text.replace(emphasized, normal)

print(text)