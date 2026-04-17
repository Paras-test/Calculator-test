# mortgage_emi.py

from typing import *
import math

class Mortgage:
    def __init__(self, principal: float, rate: float, tenure: int):
        self.principal = principal
        self.rate = rate
        self.tenure = tenure

    def calculate_emi(self) -> float:
        if not isinstance(self.principal, (int, float)) or not isinstance(self.rate, (int, float)) or not isinstance(self.tenure, int):
            raise ValueError('Invalid input. All inputs must be numbers.')
        if self.rate <= 0 or self.rate >= 1:
            raise ValueError('Rate must be between 0 and 1.')
        if self.tenure < 1:
            raise ValueError('Tenure must be at least 1 year.')

        emi = (self.principal * math.pow(1 + self.rate, self.tenure)) / ((math.pow(1 + self.rate, self.tenure) - 1) * self.rate)
        return round(emi, 2)
