def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_num_chars(text):
    num_chars = {}
    for c in text:
        c = c.lower()
        if c in num_chars:
            num_chars[c] += 1
        else:
            num_chars[c] = 1
    
    return num_chars

def sort_on(dict):
    return dict["num"]

def sort_dict(num_chars):
    dict_list = []
    for key in num_chars:
        result_dict = {}
        result_dict["char"] = key
        result_dict["num"] = num_chars[key]
        dict_list.append(result_dict)
    
    dict_list.sort(key=sort_on, reverse=True)

    return dict_list