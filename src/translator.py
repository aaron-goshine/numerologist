import re


class Translator:

    def __init__(self):
        print('done')

    def clean_string(self, string):
        return re.sub(r'[^a-zA-Z]', '', string)

    def split_on_space(self, string):
        return string.strip().split(' ')

    def char_sum(self, char_values):
        return sum(char_values)

    def tranlate_name(self, name):
        return 'lovely name, it\'s also very old'
