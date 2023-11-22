import nltk
nltk.download('punkt')

# Load your text file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\6b. One Paragraph Articles.txt", 'r', encoding='utf-8') as file:
    data = file.read().replace('\n', '')

# Tokenize into sentences
sentences = nltk.sent_tokenize(data)

# Tokenize each sentence into words
sentences_words = [nltk.word_tokenize(sentence) for sentence in sentences]

# Write tokens to a new file
with open('TOKENnolines', 'w', encoding='utf-8') as file:
    for sentence in sentences_words:
        file.write(' '.join(sentence) + '\n')