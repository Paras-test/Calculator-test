from typing import Union

class StraightLineDepreciation:
    def __init__(self, cost: float, salvage_value: float, useful_life: int):
        if cost < salvage_value or useful_life <= 0:
            raise ValueError('Invalid inputs: cost must be greater than salvage value and useful life must be positive.')
        self.cost = cost
        self.salvage_value = salvage_value
        self.useful_life = useful_life

    def calculate_depreciation(self) -> float:
        depreciation = (self.cost - self.salvage_value) / self.useful_life
        return round(depreciation, 2)