def word_counter(book):
    word_list = book.split()
    count = len(word_list)
    return count

def char_counter(book):
    char_list = list(book.lower())
    char_dict = {}
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorter(dict):
    return dict["count"]

def char_dict_lister(char_dict):
    dict_list = []
    for dict in char_dict:
        dict_list.append({'char':dict, 'count':char_dict[dict]})
    dict_list.sort(reverse=True, key=sorter)
    return dict_list