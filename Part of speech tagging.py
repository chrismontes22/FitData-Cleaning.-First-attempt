import nltk
from nltk.tokenize import word_tokenize

# Load NLTK Punkt tokenizer and averaged_perceptron_tagger
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Open your file and read the content
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKlem.txt", 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text
word_tokens = word_tokenize(text)

# Perform part-of-speech tagging
tagged_text = nltk.pos_tag(word_tokens)

# Write the tagged text to a new file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\huh.txt", 'w', encoding='utf-8') as f:
    for word, tag in tagged_text:
        f.write(f'{word}/{tag} ')
