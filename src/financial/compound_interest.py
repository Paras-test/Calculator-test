from typing import Union

class CompoundInterest:
    def __init__(self, principal: float, rate: float, years: int):
        if rate < 0 or years <= 0:
            raise ValueError('Invalid inputs: interest rate must be non-negative and years must be positive.')
        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate_compound_interest(self) -> float:
        compound_interest = self.principal * (1 + self.rate / 100) ** self.years - self.principal
        return round(compound_interest, 2)