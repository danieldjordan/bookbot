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

