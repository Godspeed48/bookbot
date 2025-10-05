import sys
from stats import (
    count_words, 
    count_char, 
    sort_dict, 
    print_alphabetical
)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    book = get_book_text(path)
    num_words = count_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = count_char(book) 
    list = sort_dict(char_dict)
    print_alphabetical(list)
    print("============= END ===============")
    
main()