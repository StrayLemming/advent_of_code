'''
23_day_4.py
https://adventofcode.com/2023

'''

from dataclasses import dataclass


@dataclass
class Card:

    num: int
    copies: int
    points: int


filename = './2023/puzzle_input_data/puzzle_input_day4.txt'
# filename = './2023/puzzle_input_data/puzzle_input_test_day4.txt'


def get_cards(filename):
    '''
    Get the puzzle data, strip any whitespace and create a card data object for each

    '''

    cards = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Split the line into 'Card' and 'Values' parts
        card_num, values = line.split(':')
        card_num = int(card_num.split()[-1])  # Get the card number

        # Split the 'Values' part into winners
        win_nums, my_nums = values.split('|')

        # win_nums = dict(winners.split())
        # Use set instead of dict. Set will remove duplicates
        win_nums = set(win_nums.split())
        my_nums = my_nums.split()

        matched = 0  # Reset for each line
        for n in win_nums:
            if n in my_nums:
                matched += 1
        # Create card object. Initially has 1 copy, this will increment in part II of the puzzle
        cards[card_num] = Card(card_num, 1, matched)

    return cards


'''
Part I
Calculate card scores
'''


def calc_card_scores(cards):
    sum_card_scores = 0

    for i in cards.keys():
        sum_card_scores += int(2**(cards[i].points-1))

    return sum_card_scores


'''
Part II
Calculate the number of cards
'''


def calc_card_counts(cards):
    sum_card_counts = 0

    for i in cards.keys():
        for j in range(cards[i].copies):
            for k in range(1, cards[i].points+1):
                cards[i+k].copies += 1
        sum_card_counts += cards[i].copies

    return sum_card_counts


cards = get_cards(filename)
print(calc_card_scores(cards))
print(calc_card_counts(cards))
