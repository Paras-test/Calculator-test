import math
from .trigonometry import sine, cosine, tangent
from .logarithm import logarithm

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise CalculatorError('Division by zero')
        return a / b

    def floor_divide(self, a, b):
        if b == 0:
            raise CalculatorError('Floor division by zero')
        return a // b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError('Modulus by zero')
        return a % b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise CalculatorError('Square root of negative number')
        return math.sqrt(a)

    def sine(self, angle):
        return sine(angle)

    def cosine(self, angle):
        return cosine(angle)

    def tangent(self, angle):
        if angle == math.pi / 2:
            raise ValueError('Tangent of pi/2 is undefined')
        return tangent(angle)

    def logarithm(self, a, base=math.e):
        if a <= 0 or base <= 1:
            raise ValueError('Logarithm of non-positive number or invalid base')
        return logarithm(a, base)