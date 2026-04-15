import math

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x > 0:
        return math.log(x)
    else:
        raise ValueError('Logarithm is not defined for non-positive numbers')