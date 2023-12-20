'''
23_day_7.1.py
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

# filename = './2023/puzzle_input_data/puzzle_input_test_day7.txt'
filename = './2023/puzzle_input_data/puzzle_input_day7.txt'

with open(filename) as f:
    data = f.readlines()

card_data = [list(line.split()) for line in data]


card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

card_combo = {'high_card': [], 'one_pair': [], 'two_pair': [],
              'three_kind': [], 'full_house': [], 'four_kind': [], 'five_kind': []}

# Get the card combos and save in their respectives lists for sorting later
for hand, bid in card_data:
    card_count = {card: hand.count(card) for card in hand}

    if 5 in card_count.values():
        card_combo['five_kind'].append((hand, int(bid)))
    elif 4 in card_count.values():
        card_combo['four_kind'].append((hand, int(bid)))
    # Full House
    elif 3 in card_count.values() and 2 in card_count.values():
        card_combo['full_house'].append((hand, int(bid)))
    elif 3 in card_count.values():
        card_combo['three_kind'].append((hand, int(bid)))
    # Cannot count on a dict, so convert to list first
    elif list(card_count.values()).count(2) == 2:
        card_combo['two_pair'].append((hand, int(bid)))
    elif 2 in card_count.values():
        card_combo['one_pair'].append((hand, int(bid)))
    else:
        card_combo['high_card'].append((hand, int(bid)))


def sort_cards(hand_type, card_values):
    return sorted(card_combo[hand_type], key=lambda x: [
        card_values[card] for card in x[0]])


def card_winnings(sorted_cards, card_index):
    return sum(
        [idx * bid[1] for idx, bid in enumerate(sorted_cards, start=card_index)])


# Sort the cards in their combos. Must pass the combos in the same order as the puzzle description to get the correct answer
sorted_cards_all = []
[sorted_cards_all.extend(sort_cards(hand_type, card_values))
 for hand_type in card_combo.keys()]

print(card_winnings(sorted_cards_all, 1))
