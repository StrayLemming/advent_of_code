# 23_day_2.py
# https://adventofcode.com/2023

# list_of_dict = []

# with open('./2023/puzzle_input_day2.txt', 'r') as puzzle_file:
#     puzzle_list = puzzle_file.read().split("\n")
#     for line in puzzle_list:
#         dict = eval(line)
#         list_of_dict.append(dict)

# print(list_of_dict)

import json

# Read the content from the text file
with open('./2023/puzzle_input_day2.txt', 'r') as file:
    content = file.readlines()

# Initialize an empty list to store dictionaries
game_list = []

# Process each line in the content
for line in content:
    # Split the line based on the colon to get the game number and the rest of the data
    game_number, game_data = line.split(':')

    # Extract individual game results by splitting based on semicolon
    results = [result.strip() for result in game_data.split(';')]

    # Initialize a dictionary for the current game
    game_dict = {'Game Number': int(game_number.strip("Game")), 'Results': []}

    # Process each result in the game and append to the dictionary
    for result in results:
        # Split each result based on commas to get color and count
        color_data = [item.strip().split() for item in result.split(',')]
        colors = {color: int(count) for count, color in color_data}
        game_dict['Results'].append(colors)

    # Append the game dictionary to the list
    game_list.append(game_dict)

# Convert the list of dictionaries to JSON format
json_data = json.dumps(game_list, indent=2)

# Print or save the JSON data
print(json_data[:1000])

# Optionally, you can save the JSON data to a file
# with open('output.json', 'w') as output_file:
#     output_file.write(json_data)
