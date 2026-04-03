import math
import logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')


class Calculator:

    def evaluate_expression(self, expression: str) -> float:
        logging.info(f'Evaluating expression: {expression}')

        try:
            return eval(expression)
        except Exception as e:
            raise CalculatorError(f"Failed to evaluate expression: {str(e)}")
    """A simple calculator providing basic arithmetic operations.

    Methods
    -------
    add(a, b)
        Return the sum of a and b.
    subtract(a, b)
        Return the difference of a and b.
    multiply(a, b)
        Return the product of a and b.
    divide(a, b)
        Return the quotient of a divided by b.
    floor_divide(a, b)
        Return the floor division of a by b.
    modulus(a, b)
        Return the modulus of a by b.
    power(a, b)
        Return a raised to the power of b.
    square_root(a)
        Return the square root of a.
    """
    def add(self, a: float, b: float) -> float:
        logging.info(f'Adding {a} and {b}')

        """Return the sum of a and b.

        Parameters
        ----------
        a : float
            First addend.
        b : float
            Second addend.

        Returns
        -------
        float
            The sum of a and b.
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        logging.info(f'Subtracting {b} from {a}')

        """Return the difference of a and b.

        Parameters
        ----------
        a : float
            Minuend.
        b : float
            Subtrahend.

        Returns
        -------
        float
            The difference a - b.
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        logging.info(f'Multiplying {a} and {b}')

        """Return the product of a and b.

        Parameters
        ----------
        a : float
            First factor.
        b : float
            Second factor.

        Returns
        -------
        float
            The product a * b.
        """
        return a * b
        
    def divide(self, a: float, b: float) -> float:
        logging.info(f'Dividing {a} by {b}')

        """Return the quotient of a divided by b.

        Parameters
        ----------
        a : float
            Dividend.
        b : float
            Divisor.

        Returns
        -------
        float
            The quotient a / b.

        Raises
        ------
        ValueError
            If b is zero.
        """
        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a / b

    def floor_divide(self, a: float, b: float) -> float:
        """Return the floor division of a by b.

        Parameters
        ----------
        a : float
            Dividend.
        b : float
            Divisor.

        Returns
        -------
        float
            The floor division a // b.

        Raises
        ------
        ValueError
            If b is zero.
        """
        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a // b

    def modulus(self, a: float, b: float) -> float:
        """Return the modulus of a by b.

        Parameters
        ----------
        a : float
            Dividend.
        b : float
            Divisor.

        Returns
        -------
        float
            The remainder a % b.

        Raises
        ------
        ValueError
            If b is zero.
        """
        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        return a % b

    def power(self, a: float, b: float) -> float:
        return a ** b
    def square_root(self, a: float) -> float:
        if a < 0:
            raise CalculatorError("Cannot take square root of negative number")
        return math.sqrt(a)

if __name__ == "__main__":
    try:
        print("10 + 5 =", calc.add(10, 5))
    except Exception as e:
        print(f"An error occurred: {e}")
    calc = Calculator()
    print("Welcome to Partial Calculator!")
    print("10 + 5 =", calc.add(10, 5))
