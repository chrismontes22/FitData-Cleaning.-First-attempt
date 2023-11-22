import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to convert nltk pos-tag to wordnet tags
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

# Input file path
input_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8c. tokenSPACYnolem.txt"

# Output file path
output_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8c. tokenSPACYlemi.txt"
# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Lemmatize each line of text
lemmatized_sentences = []
sentences = sent_tokenize(content)
for sentence in sentences:
    tokenized_sentence = word_tokenize(sentence)
    nltk_tagged = nltk.pos_tag(tokenized_sentence)  
    lemmatized_tokens = []
    for word, tag in nltk_tagged:
        wn_tag = nltk_tag_to_wordnet_tag(tag)
        if wn_tag is None:
            lemmatized_tokens.append(word)
        else:
            lemmatized_tokens.append(lemmatizer.lemmatize(word, pos=wn_tag))
    lemmatized_sentence = ' '.join(lemmatized_tokens)
    lemmatized_sentences.append(lemmatized_sentence)

# Join the lemmatized sentences back together
lemmatized_content = '\n'.join(lemmatized_sentences)

# Write the lemmatized content to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(lemmatized_content)
