#! /usr/local/bin/python3

from src.calculator import Calculator
from src.data_maps import DataMaps
from src.translator import Translator


class Main  ():

    def __init__(self):
        self.cal = Calculator()
        self.data_maps = DataMaps()
        self.translator = Translator()

    def calculateValue(self):
        print('done')

    def run(self):
        running = True
        while running:
            name = str.strip(str(input('Name? :')))
            self.cal.set_value(name)
            outexpr = self.cal.get_outter_expression()
            soul = self.cal.get_soul_urge()
            print('---------------')
            print(self.data_maps.get_vidic(outexpr))
            print('---------------')
            print(self.data_maps.get_behaviour(outexpr))
            print('---------------')
            print(self.data_maps.get_expressions(outexpr))
            print('---------------')
            print(self.data_maps.get_soul_urge(soul))
            print('---------------')

            ans = str.strip(str(input('Continue [y/n]?:')))

            if ans == 'n':
                running = False
                print('done')

            self.cal = Calculator()


if __name__ == '__main__':
    main = Main()
    main.run()
