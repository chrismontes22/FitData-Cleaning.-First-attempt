'''This code is to turn each article into one paragraph, 
basically removing all the spaces. I might try tokenizing it both with and
without spaces to see which yields better results in the end'''

def remove_newlines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip() == '<START>':
                f.write('\n<START>\n')
            elif line.strip() == '<END>':
                f.write('\n<END>\n')
            else:
                f.write(line.strip() + ' ')

# Usage
remove_newlines(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\6. Adding article breaks.txt", 'output.txt')
