```python
import math

def calculate_bmi(weight, height):
    return weight / (height ** 2)


def calculate_bmr(gender, age, weight, height, activity_level):
    if gender == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.7 * height) - (5.68 * age)
    elif gender == 'female':
        bmr = 447.6 + (9.25 * weight) + (3.09 * height) - (4.33 * age)

    if activity_level == 'sedentary':
        return bmr * 1.2
    elif activity_level == 'lightly active':
        return bmr * 1.375
    elif activity_level == 'moderately active':
        return bmr * 1.55
    elif activity_level == 'very active':
        return bmr * 1.725
    elif activity_level == 'extra active':
        return bmr * 1.9
    else:
        raise ValueError('Invalid activity level')
```
