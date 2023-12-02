# 23_day_1.py
# https://adventofcode.com/2023


with open('./2023/puzzle_input_day1.txt', 'r') as file:
    content = file.read().split("\n")


def sum_calibration_numbers(content):
    extracted_digits = []
    for line in content:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)

        extracted_digits.append(digits)

    # If there is only one digit in the list, then add to itself
    first_and_last_digits = [int(sublist[0] + sublist[-1])
                             for sublist in extracted_digits]

    total_sum = sum(first_and_last_digits)

    return total_sum


def sum_calibration_strings(content):

    # Test case
    # elf_list = "bxfour3two2sb4twondmfdpsz"

    num_str_list = [('one', 1), ('two', 2), ('three', 3), ('four', 4),
                    ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    num_sum = []

    for line in content:

        num_extract = []

        # Find will return the first instance it finds, therefore the While loop and incrementing the index will catch multiple instances of a number e.g.twotwo
        for num_str, value in num_str_list:
            index = 0
            while index != -1:
                index = line.find(num_str, index)
                if index != -1:
                    result = (value, index)
                    num_extract.append(result)
                    index += 1  # Move to the next position for the next search

        for num in num_list:
            index = 0
            while index != -1:
                index = line.find(str(num), index)
                if index != -1:
                    result = (num, index)
                    num_extract.append(result)
                    index += 1  # Move to the next position for the next search

        lowest_tuple = min(num_extract, key=lambda x: x[1])
        highest_tuple = max(num_extract, key=lambda x: x[1])
        num_concat = int(str(lowest_tuple[0]) + str(highest_tuple[0]))
        num_sum.append(num_concat)

    total_sum = sum(num_sum)
    return total_sum


print(sum_calibration_numbers(content))  # correct sum 55386
print(sum_calibration_strings(content))  # correct sum 54824
