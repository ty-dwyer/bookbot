def get_book_text(path):
    with open(path) as f:
        return f.read()


def num_words(input):
    return len(input.split())


# print(get_book_text("books/frankenstein.txt"))
print(
    f"{num_words(get_book_text('books/frankenstein.txt'))} words found in the document"
)
