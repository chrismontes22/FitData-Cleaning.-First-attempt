import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load NLTK stop words
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Open your file and read the content
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKlem.txt", 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text
word_tokens = word_tokenize(text)

# Remove stop words
filtered_text = [word for word in word_tokens if not word in stop_words]

# Write the processed text to a new file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\nltkLEMstpwrd.txt", 'w', encoding='utf-8') as f:
    f.write(' '.join(filtered_text))
