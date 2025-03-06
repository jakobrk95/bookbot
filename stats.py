def count_words(text: str):
    text_splitted = text.split()
    
    word_count = 0
    for word in text_splitted:
        word_count +=1 

    return f'{word_count} words found in the document'

def count_char(text: str):
    text = text.lower()

    chars = []
    for char in text:
        if char not in chars:
            chars.append(char)

    chars_dict = {value: 0 for value in chars}
    for char in text:
        chars_dict[char] +=1
    
    return chars_dict

# def print_report(char_list: list):
