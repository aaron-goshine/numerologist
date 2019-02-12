import unittest


from main import Main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = Main()


class TestInit(TestMain):
    def test_initial_speed(self):
        self.assertEqual(0, 0)

    def test_initial_odometer(self):
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
