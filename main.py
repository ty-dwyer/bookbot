from stats import get_num_words, get_nums_chars, sort_dict
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
print("--------- Character Count -------")
print(sort_dict(get_nums_chars(get_book_text(sys.argv[1]))))
