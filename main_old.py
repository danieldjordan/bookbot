<<<<<<< HEAD
import sys

def main(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    text = text.lower()
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

if __name__ == "__main__":
    # Check if a file path was provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_book_file>")
        sys.exit(1)
    
    # Get the file path from command line arguments
    file_path = sys.argv[1]
    
    # Process the book file
    book_text = main(file_path)
    word_count = count_words(book_text)
    letter_count = count_letters(book_text)
    
    # Print the report
    print(f"--- Begin report of {file_path} ---\n")
    print(f"{word_count} words found in the document\n\n")
    
    for letter in letter_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")
    
    print("\n--- End of report ---")

=======
from stats import count_characters, chars_dict_to_sorted_list, count_words
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

<<<<<<<< HEAD:main.py
    print("============= END ===============")

main()
========
print(
    "--- Begin report of books/frankenstein.txt ---\n"
)
print(f"{word_count} words found in the document\n\n")
for letter in letter_count:
    if letter.isalpha():
        print(f"The \'{letter}\' character was found {letter_count[letter]} times")
print("\n--- End of report ---")
>>>>>>>> 10e74f5fdc17ae42932edaa5d1c8a4d8580c08d6:main_old.py
>>>>>>> 10e74f5fdc17ae42932edaa5d1c8a4d8580c08d6
