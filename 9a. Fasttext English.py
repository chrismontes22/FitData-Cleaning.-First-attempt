"""So I am using  fastext because I felt it was a good comprimise between accuracy and computational
resources. I went with the subword model because, as with other instances, maintaining the context of data is more important to me
than capturing the nuances of language. Subword helps preserve the fitness jargon better also.
"""

''' I want to trythe english model, the wikipedia model. and also try essembling both the models.
The biggest issue is troubleshooting the installation of fasttext. Tried to force install wheels but nothing
Update: weel installation worked, got it from this edu site:
https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
'''


import fasttext

# Load the English model
english_model = fasttext.load_model(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\crawl-300d-2M-subword.bin")

# Input file path
input_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKnolem.txt"

# Output file path
output_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\9aa. NLTKenglishembedNOLEM.txt"

# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Tokenize the content (replace this with your actual tokenization logic)
tokenized_data = content.split()  # Example: split by spaces

# Generate embeddings
english_embeddings = [english_model.get_sentence_vector(sentence) for sentence in tokenized_data]

# Save the embeddings to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for embedding in english_embeddings:
        # Convert the embedding values to a comma-separated string
        embedding_str = ', '.join(map(str, embedding))
        # Write the embedding to the output file
        output_file.write(embedding_str + '\n')
