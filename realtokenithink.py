import nltk
nltk.download('punkt')

# Load your text file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\6. Adding article breaks.txt", 'r', encoding='utf-8') as file:
    data = file.read().replace('\n', '')

# Tokenize into sentences
sentences = nltk.sent_tokenize(data)

# Write tokens to a new file
with open('TOKENnolines_sentences_only.txt', 'w', encoding='utf-8') as file:
    for sentence in sentences:
        file.write(sentence + '\n')
