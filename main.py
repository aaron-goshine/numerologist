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

    def char_dataEvent(self):
        print('done')

    def ruling_dataEvent(self):
        print('done')

    def soulurge_dataEvent(self):
        print('done')

    def outerexpression_dataEvent(self):
        print('done')

    def dataEvent(self):
        print('done')

    def results_bts_click(self):
        print('done')

    def run(self):
        running = True
        while running:
            name = str.strip(str(input('Name? :')))
            self.cal.set_value(name)
            number = self.cal.get_total_value()
            print(number)

            ans = str.strip(str(input('Continue [y/n]?:')))

            if ans == 'y':
                running = False

        print('done')


if __name__ == '__main__':
    main = Main()
    main.run()
