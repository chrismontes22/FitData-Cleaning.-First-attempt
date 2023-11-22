''' Funny story about this code. To seperate  each text article in my data I used a bunch of "=" symbols.
 When I ran spaCy to get rid of proper nouns, it added spaces to all symbols. I was running the code for "=".
 Then I couldn't figure out this code for the longest of time why my code was not working.
 Turns out my dividers were now " =" with a space before the first = symbol.
 Took me  longer to figure out than doing it manually probably, but am glad I am getting better at automation.
'''

def remove_lines_starting_with(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove lines starting with " ="
    lines = [line for line in lines if not line.startswith(" =")]

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


remove_lines_starting_with("5. Nooo Contractions.txt")