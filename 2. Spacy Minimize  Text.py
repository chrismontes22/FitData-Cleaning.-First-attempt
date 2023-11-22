### This is to lower case all of the text for better tuning. I could have mixed it in with another script but that's ok.

import spacy


nlp = spacy.load("en_core_web_sm")


input_file_path = 'C:\\Users\\chris\\OneDrive\\Desktop\CODING\\Fitness App\\Txt Data Files\\3. Spell Checked.txt'

# Open the input file with utf-8 encoding
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Process the text
doc = nlp(data)

# Convert all text to lowercase
lowercase_text = doc.text.lower()

# Write the lowercase text to a new file
with open(r'C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\4. Text minimized.txt', 'w', encoding='utf-8') as file:
    file.write(lowercase_text)
