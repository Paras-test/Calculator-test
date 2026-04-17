from typing import Union

class Mortgage:
    def __init__(self, principal: float, rate: float, months: int):
        if rate < 0 or months <= 0:
            raise ValueError('Invalid inputs: interest rate must be non-negative and months must be positive.')
        self.principal = principal
        self.rate = rate
        self.months = months

    def calculate_emi(self) -> float:
        emi = (self.principal * self.rate * (1 + self.rate) ** self.months) / ((1 + self.rate) ** self.months - 1)
        return round(emi, 2)