def get_num_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_dict(char_counts):
    sorted_dicts = []
    for ch, cnt in char_counts.items():
        sorted_dicts.append({"char": ch, "num": cnt})
    def sort_on(d):
        return d["num"]
    sorted_dicts.sort(key=sort_on, reverse=True)
    return sorted_dicts

        





