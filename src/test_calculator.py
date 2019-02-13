import unittest


from calculator import Calculator


class TestInit(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_vowel_count(self):
        self.calc.set_value('string')
        expected = self.calc.get_vowel_count()
        self.assertEqual(expected, 1)

        self.calc.set_value('a')
        expected = self.calc.get_vowel_count()
        self.assertEqual(expected, 1)

        self.calc.set_value('the quick brown fox jump over the lazy dog')
        expected = self.calc.get_vowel_count()
        self.assertEqual(expected, 11)

    def test_cons_count(self):
        self.calc.set_value('the quick brown fox jump over the lazy dog')
        expected = self.calc.get_cons_count()
        self.assertEqual(expected, 23)
        self.calc.set_value('a')
        expected = self.calc.get_cons_count()
        self.assertNotEqual(expected, 1)

    def test_total_value(self):
        self.calc.set_value('a')
        expected = self.calc.get_total_value()
        self.assertEqual(expected, 1)
        self.calc.set_value('aaron')
        expected = self.calc.get_total_value()
        self.assertNotEqual(expected, 1)

    def test_characteristic(self):
        self.calc.set_value('aaron')
        expected = self.calc.get_characteristics()
        self.assertEqual(expected, 22)
        self.calc.set_value('aaron')
        expected = self.calc.get_characteristics()
        self.assertNotEqual(expected, 0)

    def test_outter_expresion(self):
        self.calc.set_value('aaron')
        expected = self.calc.get_outter_expression()
        self.assertEqual(expected, 5)

    def test_soul_urge(self):
        self.calc.set_value('aaron')
        expected = self.calc.get_soul_urge()
        self.assertEqual(expected, 8)

    def test_char_to_num(self):
        expected = self.calc.char_to_num('a')
        self.assertEqual(expected, 1)
        expected = self.calc.char_to_num('b')
        self.assertEqual(expected, 2)
        expected = self.calc.char_to_num('m')
        self.assertEqual(expected, 4)

    def test_isvowel(self):
        expected = self.calc.isvowel('a')
        self.assertTrue(expected)
        expected = self.calc.isvowel('x')
        self.assertFalse(expected)

    def test_pos_gernerator(self):
        expected = self.calc.get_pos_nums(10000111)
        self.assertListEqual(expected, [1, 1, 1, 0, 0, 0, 0, 1])

    def test_is_master_number(self):
        expected_a = self.calc.is_master_number(11)
        expected_b = self.calc.is_master_number(22)
        self.assertTrue(expected_a)
        self.assertTrue(expected_b)

    def test_ruducer(self):
        expected = self.calc.reducer(22)
        self.assertEqual(expected, 22)
        expected = self.calc.reducer(11)
        self.assertEqual(expected, 11)
        expected = self.calc.reducer(123)
        self.assertEqual(expected, 6)


if __name__ == '__main__':
    unittest.main()
