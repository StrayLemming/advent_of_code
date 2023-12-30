'''
23_day_8.1.py
https://adventofcode.com/2023
Day 8: Haunted Wasteland

'''

from itertools import cycle
# filename = './2023/puzzle_input_data/puzzle_input_test_day8.txt'
filename = './2023/puzzle_input_data/puzzle_input_day8.txt'


with open(filename) as f:
    directions, network_data = f.read().split(
        "\n\n", 1)  # Split on the first line space

# Cycle returns elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.
directions = cycle(0 if d == 'L' else 1 for d in directions)


def extract_key_value(network_data):
    nodes = {}
    network = network_data.splitlines()
    for node in network:
        # Could probably do this cleaner using regex
        key_value_str = node.replace(' ', '').replace(
            '=', ':').replace('(', '').replace(')', '')
        key, value = key_value_str.split(':')
        nodes[key] = tuple(value.split(','))

    return nodes


nodes = extract_key_value(network_data)

# Part 1
node = 'AAA'
for steps, d in enumerate(directions, start=1):
    node = nodes[node][d]
    if node == 'ZZZ':
        break

print(steps)
