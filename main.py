from stats import get_num_words
from stats import count_characters
from stats import sort_dict
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    
    char_counts = count_characters(text)
    
    sorted_dictionaries = sort_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_dictionaries:
        ch = d["char"]
        num = d["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
    