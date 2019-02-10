import json


class DataNumber:
    number_names = {
        1: "one",
        2: "three",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        11: "eleven",
        22: "twentytwo"
    }

    def __init__(self):

        self.dictionary = json.load(open('./assets/dictionary-lc.json', 'r'))
        self.behaviour = json.load(open('./data/behaviour.json', 'r'))
        self.characteristics = json.load(open('./data/characteristics.json', 'r'))
        self.dream = json.load(open('./data/dream.json', 'r'))
        self.expressions = json.load(open('./data/expressions.json', 'r'))
        self.outterexpression = json.load(open('./data/outterexpression.json', 'r'))
        self.rulingnumber = json.load(open('./data/rulingnumber.json', 'r'))
        self.soulurge = json.load(open('./data/soulurge.json', 'r'))

    def get_behaviour(self, num):
        num_name = self.number_names[num]
        return self.behaviour[num_name]

    def get_characteristic(self, num):
        num_name = self.number_names[num]
        return self.characteristics[num_name]

    def get_dream(self, num):
        num_name = self.number_names[num]
        return self.dream[num_name]

    def get_expressions(self, num):
        num_name = self.number_names[num]
        return self.expressions[num_name]

    def get_outerexpression(self, num):
        num_name = self.number_names[num]
        return self.outterexpression[num_name]

    def get_rulingnumber(self, num):
        num_name = self.number_names[num]
        return self.rulingnumber[num_name]

    def get_soulurge(self, num):
        num_name = self.number_names[num]
        return self.soulurge[num_name]