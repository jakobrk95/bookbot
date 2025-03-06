from stats import count_words, count_char

def get_book_text(path: str):
    with open(path, "r") as file:
        file_contents = file.read()    
    return file_contents

def main(path):
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))
    print(count_char(text))
    
main("books/frankenstein.txt")