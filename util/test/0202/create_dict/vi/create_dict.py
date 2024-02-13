def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

def write_file(file_path, words):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted(words)))

def merge_and_print(vi_file_path, vi_custom_file_path):
    # Read existing words from vi.txt
    existing_words = read_file(vi_file_path)

    # Read new words from vi_custom.txt
    new_words = read_file(vi_custom_file_path)

    # Remove duplicates from new words
    new_words -= existing_words

    # Merge existing and new words
    merged_words = existing_words.union(new_words)

    # Write back to vi.txt
    write_file(vi_file_path, merged_words)

    # Print newly added words
    print("Newly added words:")
    for word in new_words:
        print(fr'word :{word}')
    print(fr'완료 vi_file_path : {vi_file_path}')

# Paths to vi.txt and vi_custom.txt
vi_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\EasyOCR\easyocr\dict\vi.txt'
vi_custom_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\EasyOCR\easyocr\dict\vi_custom.txt'

# Merge and print
merge_and_print(vi_file_path, vi_custom_file_path)
