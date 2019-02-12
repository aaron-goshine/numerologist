import json
import os


class DataMaps:
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

        print(os.path.abspath('.'))
        self.behaviour = json.load(open(
            './data/behaviour.json', 'r'))

        self.characteristics = json.load(open(
            './data/characteristics.json', 'r'))

        self.dream = json.load(open('./data/dream.json', 'r'))

        self.expressions = json.load(open(
            './data/expressions.json', 'r'))

        self.outter_expression = json.load(open(
            './data/outterexpression.json', 'r'))

        self.ruling_number = json.load(open(
            './data/rulingnumber.json', 'r'))

        self.soul_urge = json.load(open(
            './data/soulurge.json', 'r'))

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

    def get_outer_expression(self, num):
        num_name = self.number_names[num]
        return self.outter_expression[num_name]

    def get_ruling_number(self, num):
        num_name = self.number_names[num]
        return self.rulingnumber[num_name]

    def get_soul_urge(self, num):
        num_name = self.number_names[num]
        return self.soul_urge[num_name]
