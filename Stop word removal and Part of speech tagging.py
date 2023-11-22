import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load NLTK stop words, Punkt tokenizer, and averaged_perceptron_tagger
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english'))

# Open your file and read the content
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKlem.txt", 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text
word_tokens = word_tokenize(text)

# Remove stop words and perform part-of-speech tagging
filtered_text = [word for word in word_tokens if not word in stop_words]
tagged_text = nltk.pos_tag(filtered_text)

# Write the tagged text to a new file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\nltkLEMsteptag2", 'w', encoding='utf-8') as f:
    for word, tag in tagged_text:
        f.write(f'{word}/{tag} ')
