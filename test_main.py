import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        data = (3,5)
        #The * operator is used to unpack the contents of data as arguments to the add method.
        result = self.calc.add(*data)
        self.assertEqual(result, 8,"Failed on adding two positive numbers.")


if __name__ == '__main__':
    unittest.main()
