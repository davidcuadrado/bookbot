from stats import get_num_words

# Function to read and return the contents of a text file
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def text_word_count(text):
    words = text.split()
    return len(words)

# Main function that reads and prints the contents of Frankenstein
def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    print(f'{num_words} words found in the document')

# Call main to run the script
if __name__ == '__main__':
    main()
