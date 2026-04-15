import unittest
from calculator import Calculator
from calculator_error import CalculatorError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertRaises(CalculatorError, self.calc.divide, 10, 0)

    def test_floor_divide(self):
        self.assertEqual(self.calc.floor_divide(10, 2), 5)
        self.assertRaises(CalculatorError, self.calc.floor_divide, 10, 0)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 2), 0)
        self.assertRaises(CalculatorError, self.calc.modulus, 10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertRaises(CalculatorError, self.calc.square_root, -1)