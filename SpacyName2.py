### My first code for erasing proper nouns to clean up the text data. 
### Erased a lot of non-proper nouns, so I need to modify that in the next version.

import spacy

def remove_irrelevant_proper_nouns(text, relevant_nouns):
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    
    tokens = [token.text if token.ent_type_ != 'PERSON' or token.text in relevant_nouns else ' ' for token in doc]

    return ' '.join(tokens).strip()

def process_large_text_file(input_file, output_file, relevant_nouns):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = remove_irrelevant_proper_nouns(content, relevant_nouns)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Example usage
input_file_path = 'Tuning data 2 spelling.txt'  # Replace with the path to your input file
output_file_path = 'Data proper Nouns Omitted.txt'  # Replace with the desired output file path
relevant_nouns = ["yoga", "other", "relevant", "nouns"]  # Add more relevant nouns as needed

process_large_text_file(input_file_path, output_file_path, relevant_nouns)

