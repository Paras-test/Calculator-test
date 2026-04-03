import math

class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
        
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def floor_divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b

    def modulus(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b

    def power(self, a: float, b: float) -> float:
        return a ** b
    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Partial Calculator!")
    print("10 + 5 =", calc.add(10, 5))
