### My test code to see how well spaCy can isolate proper nouns. I have to Automate it now for large swaths of data.
import spacy

def remove_irrelevant_proper_nouns(text, relevant_nouns):
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    # Use a list comprehension to create a list of tokens that are not 'PERSON' entities
    # or that are in the list of relevant proper nouns
    tokens = [token.text if (token.ent_type_ != 'PERSON' and token.text.lower() not in relevant_nouns) or token.text in relevant_nouns else ' ' for token in doc]

    # Join the tokens back into a single string and return it
    return ' '.join(tokens).strip()

# Test the function
text = "John Doe did Vinyasa yoga."
relevant_nouns = ["yoga"]
print(remove_irrelevant_proper_nouns(text, relevant_nouns))








