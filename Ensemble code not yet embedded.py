''' So I want to embed my text data with fasttext. I want to try
the english model, the wikipedia model. and also try essembling both the models.
The biggest issue is troubleshooting the installation of fasttext. Tried to force install wheels but nothing
Update: weel installation worked, got it from this edu site:
https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
'''

import io
import numpy as np

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = list(map(float, tokens[1:]))
    return data

# Load the models
model1 = load_vectors(r"C:\Users\chris\OneDrive\Desktop\CODING\crawl-300d-2M-subword.vec")
model2 = load_vectors(r"C:\Users\chris\OneDrive\Desktop\CODING\wiki-news-300d-1M-subword.vec")

# Input file path
input_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKnolem.txt"

# Output file path
output_file_path = '9ba. NLTKensembleembedNOLEM.txt'

# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Tokenize the content
tokenized_data = content.split()

# Generate ensemble embeddings
embeddings = []
for sentence in tokenized_data:
    embedding1 = model1.get(sentence, None)
    embedding2 = model2.get(sentence, None)
    if embedding1 is not None and embedding2 is not None:
        # Average the embeddings from the two models
        ensemble_embedding = np.mean([embedding1, embedding2], axis=0)
        embeddings.append(ensemble_embedding)

# Save the embeddings to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for embedding in embeddings:
        # Convert the embedding values to a comma-separated string
        embedding_str = ', '.join(map(str, embedding))
        # Write the embedding to the output file
        output_file.write(embedding_str + '\n')
