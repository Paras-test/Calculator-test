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
            raise ValueError("Cannot divide by zero")
        return a / b

    def floor_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b

    def power(self, a, b):
        return a ** b
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Partial Calculator!")
    print("10 + 5 =", calc.add(10, 5))
