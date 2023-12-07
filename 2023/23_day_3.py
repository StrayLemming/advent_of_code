# 23_day_3.py
# https://adventofcode.com/2023

from dataclasses import dataclass

# filename = './2023/puzzle_input_day3.txt'
filename = './2023/input_test.txt'

'''
Part I
Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

'''


@dataclass
class NumberData:
    '''
    Data Class used to store information about the numbers found in the puzzle file
    Contains a Method for shifting the start and end indices of the found number. This is needed to find
    symbols either side of the number

    '''
    number: int
    row_id: int
    row_length: int
    number_start_index: int
    number_end_index: int

    def start_index_shift(self):
        return self.number_start_index - 1 if self.number_start_index > 0 else 0

    def end_index_shift(self):
        return self.number_end_index + 2 if self.number_end_index < self.row_length else self.row_length


def get_data(filename):
    '''
    Get the puzzle data, strip any whitespace and create a list for each line
    Return and list of lists

    '''

    result_list = []

    # Read the content from the text file
    with open(filename, 'r') as file:
        content = file.readlines()

    for line in content:
        # Split the line into a list of characters, including '.'
        line_list = list(line.strip())
        # Append the list for the current line to the result_list
        result_list.append(line_list)

    list_len = len(result_list)

    return result_list


def find_numbers(input_list):
    '''
    Find the numbers in each row
    For each char in the row, check if isdigit and append to the number
    If the next char is not a digit, then convert to an integer

    Append the number data into the Data Class called NumberData

    '''

    results = []

    for row_id, row in enumerate(input_list):
        number_start_index = None
        current_number = ""

        for i, char in enumerate(row):

            if char.isdigit():
                # Start of a new number
                if number_start_index is None:
                    number_start_index = i

                current_number += char

            elif current_number:
                # End of the current number
                number_end_index = i - 1
                number = int(current_number)
                results.append(NumberData(number, row_id, len(
                    row), number_start_index, number_end_index))

                # Reset for the next number
                number_start_index = None
                current_number = ""

        # Check if there's an unfinished number at the end of the row
        if current_number:
            number_end_index = len(row) - 1
            number = int(current_number)
            results.append(NumberData(number, row_id, len(
                row), number_start_index, number_end_index))

    return results


def adjacent_symbols(number_list, numbers):
    '''
    For each number, check that boundary around it for a symbol
    Check above, below, left and right

    '''
    row_above_slice = ''
    row_below_slice = ''
    column_left = ''
    column_right = ''
    numbers_with_adjacent_symbols = []

    def _has_non_digit_char(input_str):
        '''
        Check if the string contains a symbol
        '''
        for i in range(len(input_str)):
            # Ignore '.' and check for non-digit characters
            if input_str[i] != '.' and not input_str[i].isdigit():
                return True  # Found a non-digit character
        return False  # No non-digit character found

    # Read lines above and below the given number
    for num in numbers:

        # Get the row_id below and above the number. If current row at top or bottom, then set to None
        row_id_below = num.row_id + \
            1 if num.row_id < len(number_list) - 1 else None
        row_id_above = num.row_id - 1 if num.row_id > 0 else None

        start_index_shift = num.start_index_shift()
        end_index_shift = num.end_index_shift()

        # Read row below the given number
        # Create a 'slice' of that row based on the start and end index + shift of the number position in the row
        if row_id_below is not None:
            row_below = number_list[row_id_below]
            row_below_slice = row_below[start_index_shift:end_index_shift]
            # Check for a symbol in the slice, if exists append to the list
            if _has_non_digit_char(row_below_slice):
                numbers_with_adjacent_symbols.append(num.number)
            row_below_slice = ''

        # Read row above the given number. Repeat as above
        if row_id_above is not None:
            row_above = number_list[row_id_above]
            row_above_slice = row_above[start_index_shift:end_index_shift]

            if _has_non_digit_char(row_above_slice):
                numbers_with_adjacent_symbols.append(num.number)
            row_above_slice = ''

        # Read columns left and right of the given number
        row_current = number_list[num.row_id]
        column_left = row_current[start_index_shift:num.number_start_index]
        column_right = row_current[num.number_end_index:end_index_shift]

        if _has_non_digit_char(column_left) or _has_non_digit_char(column_right):
            numbers_with_adjacent_symbols.append(num.number)
        column_left = ''
        column_right = ''

    return sum(numbers_with_adjacent_symbols)


number_list = get_data(filename)
numbers = find_numbers(number_list)
print('Numbers with adjacent symbols', adjacent_symbols(number_list, numbers))
