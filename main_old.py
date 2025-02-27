def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

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

book_text = main()
word_count = count_words(book_text)
letter_count = count_letters(book_text)

print(
    "--- Begin report of books/frankenstein.txt ---\n"
)
print(f"{word_count} words found in the document\n\n")
for letter in letter_count:
    if letter.isalpha():
        print(f"The \'{letter}\' character was found {letter_count[letter]} times")
print("\n--- End of report ---")
