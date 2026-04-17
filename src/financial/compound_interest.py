from typing import Union

def compound_interest(principal: float, rate: float, time: int) -> float:
    if principal < 0 or rate < 0 or time <= 0:
        raise ValueError('Principal, rate, and time must be non-negative and time must be positive.')
    return principal * (1 + rate / 100) ** time