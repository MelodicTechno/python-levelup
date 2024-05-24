import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workout_dict = {
    'calories': [420, 380, 390, 390],
    'duration': [50, 40, 45, 45],
    'type': ['run', 'walk', 'walk', 'run']
}
workout = pd.DataFrame(workout_dict)

workout.index = ['day1', 'day2', 'day3', 'day4',]

workout = workout.rename(columns={'calories':'Cal'})

print(workout.at['day1', 'Cal'])
