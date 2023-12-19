'''
23_day_7.py
https://adventofcode.com/2023
Day 7: Camel Cards

- Five of a kind, where all five cards have the same label: AAAAA
- Four of a kind, where four cards have the same label and one card has a different label: AA8AA
- Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
- Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
- Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
- One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
- High card, where all cards' labels are distinct: 23456


'''

import re

filename = './2023/puzzle_input_data/puzzle_input_test_day7.txt'
# filename = './2023/puzzle_input_data/puzzle_input_day7.txt'

winning_races = []

with open(filename) as f:
    data = f.readlines()


three = 'ABA2A'
four = 'AABAA'

p_five = re.compile(r'(\w)\1*.*\1.*\1.*\1.*\1')
p_four = re.compile(r'(\w)\1*.*\1.*\1.*\1')
p_three = re.compile(r'(\w)\1*.*\1.*\1')

p_two = re.compile(r'(\w)\1*.*\1')
print('three:', p_three.search(three))
print('four:', p_four.search(four))

# Full House

full = 'KKKJJ'

p_full = re.compile(r'(\w).*\1.*\1.*(\w).*\2')


m = p_five.search(full)

m = p_full.search(full)


print('searched:', m)
print('groups:', m.groups())
