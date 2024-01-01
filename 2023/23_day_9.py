'''
23_day_9.py
https://adventofcode.com/2023
Day 9: Mirage Maintenance
Part 1

I'm sure there is an algebric way of doing this?

'''
# filename = './2023/puzzle_input_data/puzzle_input_test_day9.txt'
filename = './2023/puzzle_input_data/puzzle_input_day9.txt'

with open(filename) as f:
    data = f.read()


def part1(data):

    total = 0

    for line in data.split('\n'):
        final_nums = []
        nums = [int(num) for num in line.split()]
        while set(nums) != set([0]):
            differences = []
            # Add the last number to final_nums
            final_nums.append(nums[-1])
            # Create a new list to store the differences
            for i in range(1, len(nums)):
                differences.append(nums[i] - nums[i - 1])
            nums = differences
            print(nums)
        total += sum(final_nums)

    print(total)


part1(data)
