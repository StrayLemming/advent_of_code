'''
23_day_6.py
https://adventofcode.com/2023
Day 6: Wait For It

Time:        57     72     69     92
Distance:   291   1172   1176   2026

'''

import re
from math import *
from functools import reduce

# filename = './2023/puzzle_input_data/puzzle_input_test_day6.txt'
filename = './2023/puzzle_input_data/puzzle_input_day6.txt'

winning_races = []

with open(filename) as f:
    data = f.readlines()

race_data = [[int(x) for x in re.findall(r"\d+", line)] for line in data]
races = list(zip(race_data[0], race_data[1]))
joined_races = [int(''.join(x for x in re.findall(r"\d+", line)))
                for line in data]
print(joined_races)

# My 16 year old son's lovely solution


def quadratic(n, v):
    return (ceil(((n+sqrt(n**2-4*v))/2)-1)-floor(((n-sqrt(n**2-4*v))/2)+1)+1)

# My hack job


def brute(n, v):
    count = 0
    for i in range(n):
        if ((n - i) * i) > v:
            count += 1
    return count


# # PART I
winning_races = [quadratic(n, v) for n, v in races]

# Using functools.reduce to calculate the product of the winning races
result = reduce(lambda x, y: x * y, winning_races, 1)
print(result)

# PART II
print(quadratic(*joined_races))
