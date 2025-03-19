import sys
from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text (filePath):
    with open(filePath) as b:
        content = b.read()
    return content

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein = get_book_text(sys.argv[1])
    num_words = count_words(frankenstein)
    char_count = count_char(frankenstein)
    sorted = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")

main()
