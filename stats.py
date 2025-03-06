def count_words(text: str):
    text_splitted = text.split()
    
    word_count = 0
    for word in text_splitted:
        word_count +=1 

    return f'Found {word_count} total words'

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

def sort_list(dict_to_sort):
    return dict(sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=True))
