import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_counts = sort_char_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for entry in sorted_counts:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
# Call the main function to run the program
main()

