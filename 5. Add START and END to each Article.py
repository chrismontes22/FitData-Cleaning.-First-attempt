'''Code to add a break in each article for LLM to recognize better context.
    Worked right away this time.'''

def insert_tokens(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    empty_line_count = 0
    for line in lines:
        if line.strip() == '':
            empty_line_count += 1
            if empty_line_count == 5:
                new_lines.append('<END>\n')
            elif empty_line_count == 6:
                new_lines.append('<START>\n')
        else:
            empty_line_count = 0
        new_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

insert_tokens(r"C:\Users\chris\OneDrive\Desktop\CODING\Loser.txt")
