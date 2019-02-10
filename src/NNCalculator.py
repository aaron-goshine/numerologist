import re


class NNCalculator:
        letter = 0
        splitter = 0
        finalValue = 0
        textOutPut = 0
        vowelCount = 0
        consCount = 0
        letterCount = 0
        totalValue = 0
        characteristics = 0
        soulUrge = 0
        outterExpression = 0
        initValue = 0
        intText = 0
        MST_ELEV = 11
        MST_TWNT = 22

        def __init__(self, value):
            self.initValue = value
            self.calculateValue()

        def getVowelCount(self):
            vows = re.sub(r'[^aeiou]', '', self.initValue)
            return len(vows)

        def getConsCount(self):
            vows = re.sub(r'[^bcdfghjklmnpqrstvwxyz]', '', self.initValue)
            return len(vows)

        def getTotalValue(self):
            return len(self.initValue)

        def getLetterCount(self):
            return len(self.initValue)

        def getCharacteristics(self):
            return self.reducer(self.totalValue)

        def getRulingNumber(self):
            return self.reducer(self.totalValue)

        def getBehaviour(self):
            return self.reducer(self.outterExpression)

        def getOutterExpression(self):
            return self.reducer(self.outterExpression)

        def getSoulUrge(self):
            finalValue = self.reducer(self.soulUrge)
            return finalValue.getfinalResult

        def char_to_num(letter):
            alpha = '#abcdefghijklmnopqrstuvwxyz'
            pos = alpha.index(letter)
            if pos % 11 == 0:
                return pos
            if pos % 9 == 0:
                return 9
            return pos % 9

        def isvowel(char):
            return char in ('a', 'e', 'i', 'o', 'u')

        def get_pos_nums(num):
            pos_nums = []
            while num != 0:
                pos_nums.append(num % 10)
                num = num // 10
            return pos_nums

        def is_master_number(self, num):
            return (num == self.MST_ELEV or num == self.MST_TWNT or num <= 9)

        def reducer(self, num):
            if (self.is_master_number(num)):
                return num
            htu = self.get_pos_nums(num)
            total = 0
            crushing = True
            while crushing:
                total = sum(htu)
                if (self.is_master_number(total)):
                    crushing = False
                htu = self.get_pos_nums(num)
            return total

        def calculateValue(self):
            for c in self.initValue:
                if (self.isvowel(c)):
                    self.soulUrge += self.char_to_num(c)
                else:
                    self.outterExpression += self.char_to_num(c)
                self.totalValue += self.char_to_num(c)
