# Factorial Function (Native Implementation)

This file contains the native implementation of the factorial function in Python. The logic is manually written using a loop or recursion, and it raises a standard Python ValueError for negative inputs.

```python
# Import necessary library
import math

# Define the factorial function
def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```
