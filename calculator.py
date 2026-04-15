import math

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
            raise CalculatorError('Modulus by zero')
        return a % b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise CalculatorError('Square root of negative number')
        return math.sqrt(a)

    def sine(self, angle):
        return math.sin(angle)

    def cosine(self, angle):
        return math.cos(angle)

    def tangent(self, angle):
        if angle == math.pi / 2:
            raise ValueError('Tangent is undefined at pi/2')
        return math.tan(angle)

    def logarithm(self, value, base=math.e):
        if value <= 0 or base <= 1:
            raise ValueError('Logarithm of non-positive number or invalid base')
        return math.log(value, base)