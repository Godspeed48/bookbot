def count_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    char_dict = {}

    for char in book:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict