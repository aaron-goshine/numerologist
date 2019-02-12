import unittest


from calculator import Calculator


class TestInit(unittest.TestCase):

    def test_vowel_count_pass(self):
        calc = Calculator()
        calc.set_value('string')
        expected = calc.get_vowel_count()
        self.assertEqual(expected, 1)

    def test_vowel_count_pass_a(self):
        calc = Calculator()
        calc.set_value('a')
        expected = calc.get_vowel_count()
        self.assertEqual(expected, 1)

    def test_vowel_count_fail(self):
        calc = Calculator()
        calc.set_value('b')
        expected = calc.get_vowel_count()
        self.assertNotEqual(expected, 1)

    def test_cons_count_pass(self):
        calc = Calculator()
        calc.set_value('string')
        expected = calc.get_cons_count()
        self.assertEqual(expected, 5)

    def test_cons_count_fail(self):
        calc = Calculator()
        calc.set_value('a')
        expected = calc.get_cons_count()
        self.assertNotEqual(expected, 1)

    def test_total_value_pass(self):
        calc = Calculator()
        calc.set_value('a')
        expected = calc.get_total_value()
        self.assertEqual(expected, 1)

    def test_total_value_fail(self):
        calc = Calculator()
        calc.set_value('aaron')
        expected = calc.get_total_value()
        self.assertNotEqual(expected, 1)

    def test_characteristic_past(self):
        calc = Calculator()
        calc.set_value('aaron')
        expected = calc.get_characteristics()
        self.assertEqual(expected, 22)

    def test_characteristic_fail(self):
        calc = Calculator()
        calc.set_value('aaron')
        expected = calc.get_characteristics()
        self.assertNotEqual(expected, 0)

    #
    # def test_ruling_number(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.get_nuling_number()
    #     self.assertEqual(expected, 0)
    #
    # def test_behaviour(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.get_behaviour()
    #     self.assertEqual(expected, 0)
    #
    # def test_outter_expresion(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.get_outter_expression()
    #     self.assertEqual(expected, 0)
    #
    # def test_soul_urge(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.get_soul_urge()
    #     self.assertEqual(expected, 0)
    #
    # def test_char_to_num(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.char_to_num('a')
    #     self.assertEqual(expected, 0)
    #
    # def test_isvowel(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.isvowel('a')
    #     self.assertEqual(expected, 0)
    #
    # def test_pos_gernerator(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.get_pos_nums(1)
    #     self.assertEqual(expected, 0)
    #
    # def test_is_master_number(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.is_master_number(11)
    #     self.assertEqual(expected, 0)
    #
    # def test_ruducer(self):
    #     calc = Calculator()
    #     expected = calc.set_value('string')
    #     calc.reducer(1)
    #     self.assertEqual(expected, 0)
    #

if __name__ == '__main__':
    unittest.main()
