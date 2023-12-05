'''
23_day_3.py
https://adventofcode.com/2023
Part I and Part II

Test results:
Part I = 4361
Part II = 467835

Actual results:
Part I = 532428
Part II = 84051670

Note to self: next time split the functions as they were getting too big and messy

'''

from dataclasses import dataclass
from typing import List

filename = './2023/puzzle_input_day3.txt'
# filename = './2023/puzzle_input_test_day3.txt'


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


@dataclass
class GearData:
    '''
    Data Class used to store information about the gears (*) found in the puzzle file
    Contains a Method for multiplying the 2 x gears found (the gear ratio)

    '''
    gear_id: int
    gear_nums: List[str]

    def gear_ratio(self):
        if len(self.gear_nums) == 2:
            return self.gear_nums[0]*self.gear_nums[1]
        else:
            return None


def get_data(filename):
    '''
    Get the puzzle data, strip any whitespace and create a list for each line
    Return and list of lists

    '''

    result_list = []

    with open(filename, 'r') as file:
        content = file.readlines()

    for line in content:
        line_list = list(line.strip())
        result_list.append(line_list)

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
    For Part I:
    For each number, check that boundary around it for any symbol
    Check row above and below the number
    Check column left and right the number


    For Part II:
    If we find a gear (*) symbol, get the co-ordinates and save to GearData class object

    '''

    numbers_with_adjacent_symbols = []
    gears_with_numbers = []

    def _has_non_digit_char(row_id, row, start_idx, end_idx):
        '''
        Check if the string contains any symbol or gear
        '''
        symbol_found = False
        gear_found = False
        gear_id = None

        for i in range(start_idx, end_idx):
            # Ignore '.' and check for non-digit characters
            # Check i is less than row length otherwise IndexError
            if 0 <= i < len(row):

                if row[i] != '.' and not row[i].isdigit():
                    symbol_found = True  # Found a non-digit character

                    if row[i] == '*':
                        gear_found = True  # Found a gear (*)
                        # Record the x,y co-ords of the gear
                        gear_id = (i, row_id)

        return symbol_found, gear_found, gear_id

    def _find_gear(gears_with_numbers, gear_id, num):
        '''
        Check if the gear_id already exists in the gears_with_numbers list
        If exists, then append the number to the gear object (thus associating the number with the gear)
        Else create a new gear object
        '''

        for gear_data in gears_with_numbers:
            if gear_data.gear_id == gear_id:
                # Gear ID found, append the number to the existing GearData object
                gear_data.gear_nums.append(num.number)
                return True

        # Gear ID not found, create a new GearData object and append it to gears_with_numbers list
        gears_with_numbers.append(GearData(gear_id, [num.number]))
        return False

    def _calc_gear_ratio(gears_with_numbers):
        '''
        Calc the gear ratio by calling the GearData.gear_ratio method, return the sum
        '''
        return sum((gear.gear_ratio() for gear in gears_with_numbers if gear.gear_ratio() != None), 0)

    '''
    Read lines above & below the given number including diagnoally (the start_index_shift and end_index_shift)
    Read columns left and right the given number
    '''
    for num in numbers:

        # Get the row_id below and above the number. If current row at top or bottom, then set to None
        row_id_below = num.row_id + \
            1 if num.row_id < len(number_list) - 1 else None
        row_id_above = num.row_id - 1 if num.row_id > 0 else None

        start_index_shift = num.start_index_shift()
        end_index_shift = num.end_index_shift()

        # Read row below the given number
        if row_id_below is not None:
            row_below = number_list[row_id_below]

            symbol_found, gear_found, gear_id = _has_non_digit_char(
                row_id_below, row_below, start_index_shift, end_index_shift)

            # If a symbol is found add to the numbers_with_adjacent_symbols list
            numbers_with_adjacent_symbols.append(
                num.number) if symbol_found else []

            # If a gear is found append GearData object (inc number and gear_id) to the gears_with_numbers list
            _find_gear(gears_with_numbers, gear_id, num) if gear_found else []

        # Read row above the given number. Repeat as above
        if row_id_above is not None:
            row_above = number_list[row_id_above]

            symbol_found, gear_found, gear_id = _has_non_digit_char(
                row_id_above, row_above, start_index_shift, end_index_shift)

            numbers_with_adjacent_symbols.append(
                num.number) if symbol_found else []

            _find_gear(gears_with_numbers, gear_id, num) if gear_found else []

        # Read columns left and right of the given number
        row_current = number_list[num.row_id]
        symbol_found_left, gear_found_left, gear_id = _has_non_digit_char(
            num.row_id, row_current, start_index_shift, num.number_start_index)

        _find_gear(gears_with_numbers, gear_id, num) if gear_found_left else []

        symbol_found_right, gear_found_right, gear_id = _has_non_digit_char(
            num.row_id, row_current, num.number_end_index, end_index_shift)

        _find_gear(gears_with_numbers, gear_id,
                   num) if gear_found_right else []

        numbers_with_adjacent_symbols.append(
            num.number) if symbol_found_left or symbol_found_right else []

    return sum(numbers_with_adjacent_symbols), _calc_gear_ratio(gears_with_numbers)


number_list = get_data(filename)
numbers = find_numbers(number_list)
sum_adjacent_symbols, sum_gears = adjacent_symbols(number_list, numbers)
print('Sum of numbers with adjacent symbols (part I): ', sum_adjacent_symbols,
      '\nSum of number gear ratios (part II): ', sum_gears)
