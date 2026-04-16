# Unit Tests for the Factorial Function

This file contains unit tests for the factorial function in test_calculator.py. The tests cover scenarios such as factorial(0), a positive integer, and handling negative inputs.

```python
import unittest
from calculator import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
```
