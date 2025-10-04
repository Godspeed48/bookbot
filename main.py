from stats import count_words, count_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    num_words = count_words(book)
    print(f"Found {num_words} total words")
    char_dict = count_char(book)
    print(char_dict)
    
main()