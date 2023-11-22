def get_embedding_dimensionality(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        header = file.readline()
        return int(header.strip().split()[1])

file1_path = r"C:\Users\chris\OneDrive\Desktop\CODING\crawl-300d-2M-subword.vec"
file2_path = r"C:\Users\chris\OneDrive\Desktop\CODING\wiki-news-300d-1M-subword.vec"

dimensionality1 = get_embedding_dimensionality(file1_path)
dimensionality2 = get_embedding_dimensionality(file2_path)

if dimensionality1 == dimensionality2:
    print("Both files have the same dimensionality.")
else:
    print("The files have different dimensionality.")
