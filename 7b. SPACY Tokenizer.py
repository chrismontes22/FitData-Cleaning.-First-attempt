import spacy

# Load English tokenizer
nlp = spacy.load('en_core_web_sm')

# Load your text file
with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\6b. One Paragraph Articles.txt", 'r', encoding='utf-8') as file:
    data = file.read().replace('\n', '')

# Tokenize into sentences
doc = nlp(data)
sentences = list(doc.sents)

# Tokenize each sentence into words
sentences_words = [[token.text for token in sentence] for sentence in sentences]

# Write tokens to a new file
with open('spacyTOKENnolines.txt', 'w', encoding='utf-8') as file:
    for sentence in sentences_words:
        file.write(' '.join(sentence) + '\n')
