from stats import count_words, count_char, sort_list
import sys

def get_book_text(path: str):
    with open(path, "r") as file:
        file_contents = file.read()    
    return file_contents

def alpha_dict(dict):
    filtered_chars = {char: count for char, count in dict.items() if char.isalpha()}
    return filtered_chars

def main(path):
    text = get_book_text(path)
    chars = count_char(text)
    ordered_chars = sort_list(chars)    
    dict_output = alpha_dict(ordered_chars)

    print('============ BOOKBOT ============ \n'
          f'Analyzing book found at {path}... \n'
          '----------- Word Count ----------')   
    print(count_words(text))
    print('--------- Character Count -------')
    
    for key, value in dict_output.items():
        print(f'{key}: {value}') 
    
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
    

    

