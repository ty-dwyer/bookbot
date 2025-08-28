from collections import defaultdict


def get_num_words(input):
    return len(input.split())


def get_nums_chars(input):
    char_dict = defaultdict(int)
    new_input = input.lower()
    for i in range(0, len(new_input)):
        char_dict[new_input[i]] += 1
    return char_dict


def sort_dict(d):
    filtered = {k: v for k, v in d.items() if k.isalpha()}
    new_dict = sorted(filtered.items())
    for k, v in new_dict:
        print(f"{k}: {v}")
