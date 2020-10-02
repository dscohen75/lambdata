"""Lambdata - a collection of Data Science helper functions"""

import pandas as pd
import numpy as np

favorite_animals = ['cat','dog','sloth', 'giraffe','zebra']

COLORS = ("Blue", "Orange", "Red", "Green", "Violet", "Cyan")

TEST_DF = pd.DataFrame([[2,5],
                        [8,3],
                        [9,4],
                        [5,2],
                        [2,9],
                        [9,2],
                        [3,4],
                        [6,1],
                        [3,7]], columns = ['AA', 'BB'])

def increment(number):
    """Increases a give number by 1."""
    return number + 1


