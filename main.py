import sys
from sys import argv
from stats import word_counter
from stats import char_counter
from stats import sort_chars_counts_list


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_frankenstein = get_book_text(argv[1])
    print(f"Analyzing book found at {argv[1]}...")
    frankenstein_word_count = word_counter(book_frankenstein)
    frankenstein_char_count = char_counter(book_frankenstein)
    sorted_frankenstein_char_count= sort_chars_counts_list(frankenstein_char_count)
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")
    #print(frankenstein_char_count)
    for char_count in sorted_frankenstein_char_count:
        char = char_count["char"]
        count = char_count["num"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()