import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()    # do something with f (the file) here
    return file_contents

from stats import count_words

from stats import count_char

from stats import sort_char_counts

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    num_char = count_char(text)
    sorted_chars = sort_char_counts(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
'''    for char, count in num_char.items():
        print(f"'{char}': {count}")
'''
main()