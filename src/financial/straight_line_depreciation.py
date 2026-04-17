```python
from typing import Union, Tuple

def straight_line_depreciation(cost: float, salvage_value: float, useful_life: int) -> float:
    if cost <= 0 or salvage_value >= cost or useful_life <= 0:
        raise ValueError('Invalid inputs for straight-line depreciation calculation')
    return (cost - salvage_value) / useful_life
```