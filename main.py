import sys
from stats import count_words, count_chars, get_report_dict


def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(filepath):
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_dict = count_chars(book_text)
    report_dict = get_report_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in report_dict:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print_report(filepath)


main()
