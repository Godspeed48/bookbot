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

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dicts = []
    for i in dict:
        tmp = {"name": i, "num": dict[i]}
        dicts.append(tmp)

    dicts.sort(reverse=True, key=sort_on)
    return dicts

def print_alphabetical(list):
    for d in list:
        if not d["name"].isalpha():
            continue
        else:
            print(f"{d["name"]}: {d["num"]}")