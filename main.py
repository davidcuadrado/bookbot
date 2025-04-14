from stats import get_num_words, character_count, print_report
import sys

# Function to read and return the contents of a text file
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def text_word_count(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_path = sys.argv[1]
    book_text = get_book_text(text_path)
    num_words = get_num_words(book_text)
    print(f'{num_words} words found in the document')
    character_recount = character_count(book_text)
    print(character_recount)
    print_report(book_text, text_path)

# Call main to run the script
if __name__ == '__main__':
    main()
