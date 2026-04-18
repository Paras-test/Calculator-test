# src/kinematics.py
import math

def calculate_final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def calculate_displacement(initial_position, initial_velocity, acceleration, time):
    return initial_position + (initial_velocity * time) + (0.5 * acceleration * time ** 2)

def calculate_acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time