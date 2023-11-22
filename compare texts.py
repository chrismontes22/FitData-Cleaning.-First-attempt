def compare_text_files(file1_path, file2_path):
    # Read the contents of the first file
    with open(file1_path, 'r', encoding='utf-8') as file1:
        content1 = file1.readlines()

    # Read the contents of the second file
    with open(file2_path, 'r', encoding='utf-8') as file2:
        content2 = file2.readlines()

    # Compare the contents line by line
    for i, (line1, line2) in enumerate(zip(content1, content2), start=1):
        if line1 != line2:
            print(f"Files differ at line {i}:\nFile 1: {line1.strip()}\nFile 2: {line2.strip()}")
            return False

    # Check if the files have different lengths
    if len(content1) != len(content2):
        print("Files have different lengths.")
        return False

    print("Files are identical.")
    return True

# Example usage
file1_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\nltkLEMsteptag.txt"
file2_path = r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\nltkLEMsteptag2"
compare_result = compare_text_files(file1_path, file2_path)

if compare_result:
    print("The files are the same.")
else:
    print("The files are different.")
