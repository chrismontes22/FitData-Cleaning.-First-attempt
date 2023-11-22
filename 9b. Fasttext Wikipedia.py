import io

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = list(map(float, tokens[1:]))
    return data

# Load the English model
english_model = load_vectors(r"C:\Users\chris\OneDrive\Desktop\CODING\wiki-news-300d-1M-subword.vec")

# Input file path
input_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKnolem.txt"

# Output file path
output_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\9ba. NLTKnolemWIKIEMBED.txt.txt"

# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Tokenize the content (replace this with your actual tokenization logic)
tokenized_data = content.split()  # Example: split by spaces

# Generate embeddings
english_embeddings = [english_model.get(sentence, None) for sentence in tokenized_data]

# Save the embeddings to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for embedding in english_embeddings:
        if embedding is not None:
            # Convert the embedding values to a comma-separated string
            embedding_str = ', '.join(map(str, embedding))
            # Write the embedding to the output file
            output_file.write(embedding_str + '\n')
