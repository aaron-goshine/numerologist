import re


class Calculator:

    outter_expression = 0
    total_value = 0
    soul_urge = 0

    def set_value(self, value):
        self.init_value = value
        self.calculate()

    def get_vowel_count(self):
        vows = re.sub(r'[^aeiou]', '', self.init_value)
        return len(vows)

    def get_cons_count(self):
        vows = re.sub(r'[^bcdfghjklmnpqrstvwxyz]', '', self.init_value)
        return len(vows)

    def get_total_value(self):
        return self.reducer(self.total_value)

    def get_characteristics(self):
        return self.reducer(self.total_value)

    def get_nuling_number(self):
        return self.reducer(self.total_value)

    def get_behaviour(self):
        return self.reducer(self.outter_expression)

    def get_outter_expression(self):
        return self.reducer(self.outter_expression)

    def get_soul_urge(self):
        final_value = self.reducer(self.soul_urge)
        return final_value.getfinal_result

    def char_to_num(self, letter):
        alpha = '#abcdefghijklmnopqrstuvwxyz'
        pos = alpha.index(letter)
        if pos % 11 == 0:
            return pos
        if pos % 9 == 0:
            return 9
        return pos % 9

    def isvowel(self, char):
        return char in ('a', 'e', 'i', 'o', 'u')

    def get_pos_nums(self, num):
        pos_nums = []
        while num != 0:
            pos_nums.append(num % 10)
            num = num // 10
        return pos_nums

    def is_master_number(self, num):
        return (num == 11 or num == 22 or num <= 9)

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

    def calculate(self):
        for c in self.init_value:
            if (self.isvowel(c)):
                self.soul_urge += self.char_to_num(c)
            else:
                self.outter_expression += self.char_to_num(c)
            self.total_value += self.char_to_num(c)
