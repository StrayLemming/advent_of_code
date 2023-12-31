'''
23_day_8.py
https://adventofcode.com/2023
Day 8: Haunted Wasteland
Part 1 and 2

'''

from itertools import cycle
import math

# filename = './2023/puzzle_input_data/puzzle_input_test_day8.txt'
filename = './2023/puzzle_input_data/puzzle_input_day8.txt'


with open(filename) as f:
    directions, network_data = f.read().split(
        "\n\n", 1)  # Split on the first line space

# Cycle returns elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.
# Use 0 and 1 instead of L and R directions to make looping easier
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


def part1():
    # Part 1
    node = 'AAA'
    for steps, d in enumerate(directions, start=1):
        node = nodes[node][d]
        if node == 'ZZZ':
            break

    print(steps)


def part2():
    # Get the starting nodes if the last char == A
    start_nodes = [node for node in nodes if node[2] == 'A']
    cycles = []
    for node in start_nodes:
        for steps, d in enumerate(directions, start=1):
            node = nodes[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    # Calculate LCM using math.lcm.
    # The *cycles syntax is used to unpack the list elements and pass them as separate arguments to the math.lcm function.
    lcm_result = math.lcm(*cycles)
    print(lcm_result)


def lcm_tutorial():
    '''
    The Least Common Multiple (LCM) of two or more integers is the smallest positive integer that is divisible by each of the given numbers without leaving a remainder.
    In other words, it is the smallest common multiple of the numbers.
    For example, consider the numbers 4 and 5.
    The multiples of 4 are 4, 8, 12, 16, 20, 24, and so on.
    The multiples of 5 are 5, 10, 15, 20, 25, and so on.
    The LCM of 4 and 5 is 20 because it is the smallest number that is a multiple of both 4 and 5.

    '''
    a = 4
    b = 5
    c = 10

    # Calculate LCM of three numbers using math.lcm
    lcm_ab = math.lcm(a, b)
    lcm_abc = math.lcm(lcm_ab, c)

    print("LCM of", a, b, c, "is:", lcm_abc)


part1()
part2()
lcm_tutorial()
