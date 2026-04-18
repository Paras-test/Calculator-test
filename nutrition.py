# nutrition.py

def calculate_daily_calories(weight, height, age, sex, activity_level):
    # BMR calculation based on Mifflin-St Jeor formula
    if sex == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity level multipliers
    if activity_level == 'sedentary':
        multiplier = 1.2
    elif activity_level == 'lightly active':
        multiplier = 1.375
    elif activity_level == 'moderately active':
        multiplier = 1.55
    elif activity_level == 'very active':
        multiplier = 1.725
    else:
        raise ValueError('Invalid activity level')

    # Calculate daily caloric needs
    return bmr * multiplier