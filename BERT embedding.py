from transformers import BertTokenizer, BertModel
import torch
import numpy as np

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load pre-trained model (weights)
model = BertModel.from_pretrained('bert-base-uncased')

# Put the model in "evaluation" mode, meaning feed-forward operation.
model.eval()

def embed_text(text):
    # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    input_ids = tokenizer.encode(text, add_special_tokens=True)
    input_ids = torch.tensor([input_ids])  # Add batch dimension

    # Predict hidden states features for each layer
    with torch.no_grad():
        outputs = model(input_ids)

    # Get the embeddings of the last layer
    last_layer_embeddings = outputs[0]

    # Calculate the mean of the embeddings
    mean_embedding = torch.mean(last_layer_embeddings, dim=1)

    return mean_embedding.numpy()

# Path to the input text file
input_file_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\8a. tokenNLTKnolem.txt"

# Path to the output embeddings file
output_file_path = 'output_embeddings.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        # Remove trailing newline
        line = line.rstrip()

        # Generate embeddings for the line
        embedding = embed_text(line)

        # Convert the embedding to a comma-separated string
        embedding_str = ', '.join(map(str, embedding.flatten()))

        # Write the line and its embedding to the output file
        output_file.write(line + ': ' + embedding_str + '\n')
