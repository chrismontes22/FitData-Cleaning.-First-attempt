import numpy as np

def concatenate_embeddings(file1, file2, output_file):
    # Load the embeddings
    embedding1 = np.load(file1)
    embedding2 = np.load(file2)

    # Concatenate the embeddings
    combined_embedding = np.concatenate((embedding1, embedding2))

    # Save the combined embedding
    np.save(output_file, combined_embedding)

# Usage:
concatenate_embeddings('path_to_embedding1.npy', 'path_to_embedding2.npy', 'path_to_output.npy')

#make sure to save as npy paths not .txt files