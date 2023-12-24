'''
23_day_7.2.py
https://adventofcode.com/2023
Day 7: Camel Cards Part II

J is a wild card

Tricky card combos!
jjj23
jj234

'''

# filename = './2023/puzzle_input_data/puzzle_input_test_day7.txt'
filename = './2023/puzzle_input_data/puzzle_input_day7.txt'

with open(filename) as f:
    data = f.readlines()

card_data = [list(line.split()) for line in data]

# Part II - Changed J to be the weakest card
card_values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}

card_combo = {'high_card': [], 'one_pair': [], 'two_pair': [],
              'three_kind': [], 'full_house': [], 'four_kind': [], 'five_kind': []}


def count_cards(hand):
    return {card: hand.count(card) for card in hand}


def is_joker(card_count):
    return card_count.get('J', 0)


def check_combos(hand, bid):
    card_count = count_cards(hand)
    j_count = is_joker(card_count)

    if 5 in card_count.values():
        card_combo['five_kind'].append((hand, int(bid)))

    elif 4 in card_count.values():
        if j_count == 1 or j_count == 4:
            card_combo['five_kind'].append((hand, int(bid)))
        else:
            card_combo['four_kind'].append((hand, int(
                bid)))

    elif 3 in card_count.values() and 2 in card_count.values():
        if j_count == 2 or j_count == 3:
            card_combo['five_kind'].append((hand, int(bid)))

        else:
            card_combo['full_house'].append((hand, int(bid)))

    elif 3 in card_count.values():
        if j_count == 1 or j_count == 3:
            card_combo['four_kind'].append((hand, int(bid)))
        else:
            card_combo['three_kind'].append((hand, int(bid)))

    elif list(card_count.values()).count(2) == 2:
        if j_count == 2:
            card_combo['four_kind'].append((hand, int(bid)))
        elif j_count == 1:
            card_combo['full_house'].append((hand, int(bid)))
        else:
            card_combo['two_pair'].append((hand, int(bid)))

    elif 2 in card_count.values():
        if j_count == 1 or j_count == 2:
            card_combo['three_kind'].append((hand, int(bid)))
        else:
            card_combo['one_pair'].append((hand, int(bid)))

    elif j_count == 1:
        card_combo['one_pair'].append((hand, int(bid)))
    else:
        card_combo['high_card'].append((hand, int(bid)))


def sort_cards(hand_type, card_values):
    return sorted(card_combo[hand_type], key=lambda x: [
        card_values[card] for card in x[0]])


def card_winnings(sorted_cards, card_index):
    return sum(
        [idx * bid[1] for idx, bid in enumerate(sorted_cards, start=card_index)])


for hand, bid in card_data:
    check_combos(hand, bid)

# Sort the cards in their combos. Must pass the combos in the same order as the puzzle description to get the correct answer
sorted_cards_all = []
[sorted_cards_all.extend(sort_cards(hand_type, card_values))
 for hand_type in card_combo.keys()]

print(card_winnings(sorted_cards_all, 1))
