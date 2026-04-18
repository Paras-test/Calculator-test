import math

def calculate_target_heart_rate(age, resting_hr):
    max_hr = 208 - (0.7 * age)
    target_hr = (max_hr - resting_hr) * 0.5 + resting_hr
    return target_hr