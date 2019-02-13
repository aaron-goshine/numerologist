import re


class Translator:

    def __init__(self):
        print('done')

    @staticmethod
    def clean_string(string):
        return re.sub(r'[^a-zA-Z]', '', string)

    @staticmethod
    def split_on_space(string):
        return string.strip().split(' ')
