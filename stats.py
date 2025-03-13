def word_counter(book_text):
    return len(book_text.split())

def char_counter(book_text):
    char_counts = {}
    for char in book_text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_chars_counts_list(char_counts):
    char_counts_list = []
    for char in char_counts:
        if char.isalpha():
            char_counts_list.append({"char": char, "num": char_counts[char]})


    return sorted(char_counts_list, reverse=True, key=sort_on)