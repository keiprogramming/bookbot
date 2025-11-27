
def get_num_words(text_str: str) -> int:
    split_words_list = text_str.split()
    count_words = len(split_words_list)
    return count_words

def count_letter(txt_str: str) -> dict:
    characters = list(txt_str.lower())
    char_dict = {}
    for char in characters:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict[char] + 1
    return char_dict

def helper_func(e: tuple) -> int:
    return e[1]

def sort_dict(char_dict: dict) -> list:
    s_list = char_dict.items()
    n_list = []
    for key, item in s_list:
        temp_tuple = (key, item)
        n_list.append(temp_tuple)
    n_list.sort(reverse=True, key=helper_func)
    return n_list
    
    

