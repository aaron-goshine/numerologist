import re


def clean_string(string):
    return re.sub(r'[^a-zA-Z]', '', string)


def split_on_space(string):
    return string.strip().split(' ')


def char_sum(char_values):
    return sum(char_values)
