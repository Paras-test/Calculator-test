import pytest
import math
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

    def test_sine_values(self):
        assert self.calc.sine(0.0) == pytest.approx(0.0)
        assert self.calc.sine(math.pi / 2) == pytest.approx(1.0)

    def test_cosine_values(self):
        assert self.calc.cosine(0.0) == pytest.approx(1.0)
        assert self.calc.cosine(math.pi) == pytest.approx(-1.0)

    def test_tangent_values(self):
        assert self.calc.tangent(0.0) == pytest.approx(0.0)

    def test_tangent_undefined(self):
        with pytest.raises(ValueError):
            self.calc.tangent(math.pi / 2)

    def test_logarithm_values(self):
        assert self.calc.logarithm(100.0, 10.0) == pytest.approx(2.0)
        assert self.calc.logarithm(math.e) == pytest.approx(1.0)

    def test_logarithm_invalid_inputs(self):
        with pytest.raises(ValueError):
            self.calc.logarithm(0.0)
        with pytest.raises(ValueError):
            self.calc.logarithm(-1.0)
        with pytest.raises(ValueError):
            self.calc.logarithm(10.0, 1.0)