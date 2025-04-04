import sys
from stats import get_num_words, get_num_chars, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(file_path, word_count, char_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in char_count_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count_list = sort_dict(get_num_chars(book_text))
    print_report(file_path, word_count, char_count_list)

main()