import re

def remove_extra_empty_lines(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'\n\s*\n', '\n\n', text)
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(text)

# Usage
remove_extra_empty_lines(r"text file here")
