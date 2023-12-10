'''
23_day_5.2.py
https://adventofcode.com/2023
Day 5: If You Give A Seed A Fertilizer

This stumped me.
credit to: https://www.reddit.com/r/adventofcode/comments/18b4b0r/2023_day_5_solutions/kc9ggxh/?context=3
Very elegant solution

'''

import re

filename = './2023/puzzle_input_data/puzzle_input_test_day5.txt'
# filename = './2023/puzzle_input_data/puzzle_input_day5.txt'


def locations(intervals):
    for maps_block in input_maps.split("\n\n"):
        mappings = [[int(x) for x in rules.split()]
                    for rules in maps_block.split("\n")[1:]]
        images = list()
        while intervals:
            x, y = intervals.pop()
            for mapping in mappings:
                a, b, delta = mapping
                c = b + delta - 1
                t = b - a
                # Required for Part I
                if b <= x <= y <= c:
                    images.append((x - t, y - t))
                    break
                # Next two conditions required for Part II
                elif b <= x <= c < y:
                    images.append((x - t, c - t))
                    intervals.append((c + 1, y))
                    break
                elif x < b <= y <= c:
                    images.append((b - t, y - t))
                    intervals.append((x, b - 1))
                    break
            else:
                images.append((x, y))
        intervals = images
    return intervals


with open(filename) as f:
    input_seeds, input_maps = f.read().split(
        "\n\n", 1)  # Split on the first occurance \n\n

# ========= PART 1 ==========
seed_data = [int(x) for x in re.findall(r"\d+", input_seeds)]
print(min(min(locations([(x, x) for x in seed_data]))))

# ========= PART 2 ==========
seed_intervals = [(x, x + d - 1)
                  for x, d in zip(seed_data[::2], seed_data[1::2])]
print(min(min(locations(seed_intervals))))
