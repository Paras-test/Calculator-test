import math
from calculator_error import CalculatorError
import logging
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def log(x):
    if x <= 0:
        raise CalculatorError('Cannot take logarithm of non-positive number')
    return math.log(x)
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')
class Calculator:

    def evaluate_expression(self, expression: str) -> float:
        logging.info(f'Evaluating expression: {expression}')

        try:
            return eval(expression)
        except Exception as e:
            raise CalculatorError(f"Failed to evaluate expression: {str(e)}")
    def add(self, a: float, b: float) -> float:
        logging.info(f'Adding {a} and {b}')

        return a + b

    def subtract(self, a: float, b: float) -> float:
        logging.info(f'Subtracting {b} from {a}')

        return a - b

    def multiply(self, a: float, b: float) -> float:
        logging.info(f'Multiplying {a} and {b}')

        return a * b

    def divide(self, a: float, b: float) -> float:
        logging.info(f'Dividing {a} by {b}')

        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a / b

    def floor_divide(self, a: float, b: float) -> float:
        logging.info(f'Floor dividing {a} by {b}')

        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a // b

    def modulus(self, a: float, b: float) -> float:
        logging.info(f'Modulus of {a} by {b}')

        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a % b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def square_root(self, a: float) -> float:
        if a < 0:
            raise CalculatorError("Cannot take square root of negative number")
        return math.sqrt(a)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def log(x):
    if x <= 0:
        raise CalculatorError('Cannot take logarithm of non-positive number')
    return math.log(x)
if __name__ == "__main__":
    try:
        print("10 + 5 =", calc.add(10, 5))
    except Exception as e:
        print(f"An error occurred: {e}")
calc = Calculator()
print("Welcome to Partial Calculator!")
print("10 + 5 =", calc.add(10, 5))