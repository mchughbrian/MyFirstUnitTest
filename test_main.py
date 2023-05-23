import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        data = [3,5]
        #The * operator is used to unpack the contents of data as arguments to the add method.
        result = self.calc.add(*data)
        self.assertEqual(result, 8,"Failed on adding two positive numbers.")

        data = [-1, 1]
        result = self.calc.add(*data)
        self.assertEqual(result, 0, "Failed on adding a negative and a positive number.")

        data = [0, 0]
        result = self.calc.add(*data)
        self.assertEqual(result, 0, "Failed on adding two zeros.")

        data = [-1, -1]
        result = self.calc.add(*data)
        self.assertEqual(result, -2, "Failed on adding two negative numbers.")

        # Testing with a string input
        with self.assertRaises(ValueError):
            data = ['a', 1]
            self.calc.add(*data)

        # Testing with None input
        with self.assertRaises(ValueError):
            data = [None, 1]
            self.calc.add(*data)

    def test_subtract(self):
        data = [5, 3]
        # The * operator is used to unpack the contents of data as arguments to the add method.
        result = self.calc.subtract(*data)
        self.assertEqual(result, 2, "Failed on subtracting two positive numbers.")

        data = [-1, 1]
        result = self.calc.subtract(*data)
        self.assertEqual(result, -2, "Failed on subtracting a negative and a positive number.")

        data = [0, 0]
        result = self.calc.subtract(*data)
        self.assertEqual(result, 0, "Failed on subtracting two zeros.")

        data = [-1, -1]
        result = self.calc.subtract(*data)
        self.assertEqual(result, 0, "Failed on subtracting two negative numbers.")

        # Testing with a string input
        with self.assertRaises(ValueError):
            data = ['a', 1]
            self.calc.subtract(*data)

        # Testing with None input
        with self.assertRaises(ValueError):
            data = [None, 1]
            self.calc.subtract(*data)

    def test_multiply(self):
        data = [5, 3]
        # The * operator is used to unpack the contents of data as arguments to the add method.
        result = self.calc.multiply(*data)
        self.assertEqual(result, 15, "Failed on multiplying two positive numbers.")

        data = [-5, 1]
        result = self.calc.multiply(*data)
        self.assertEqual(result, -5, "Failed on multiplying a negative and a positive number.")

        data = [0, 0]
        result = self.calc.multiply(*data)
        self.assertEqual(result, 0, "Failed on multiplying two zeros.")

        data = [-1, -1]
        result = self.calc.multiply(*data)
        self.assertEqual(result, 1, "Failed on multiplying two negative numbers.")

        # Testing with a string input
        with self.assertRaises(ValueError):
            data = ['a', 1]
            self.calc.multiply(*data)

        # Testing with None input
        with self.assertRaises(ValueError):
            data = [None, 1]
            self.calc.multiply(*data)

if __name__ == '__main__':
    unittest.main()
