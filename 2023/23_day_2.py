# 23_day_2.py
# https://adventofcode.com/2023

import json

# Max number of cubes per game
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

# Read the content from the text file
with open('./2023/puzzle_input_day2.txt', 'r') as file:
    content = file.readlines()

# Test data
# with open('./2023/test_input.txt', 'r') as file:
#     test_content = file.readlines()


def create_json(content):

    # Initialize an empty list to store dictionaries
    game_list = []

    # Process each line in the content
    for line in content:
        # Split the line based on the colon to get the game number and the rest of the data
        game_number, game_data = line.split(':')

        # Extract individual game results by splitting based on semicolon
        results = [result.strip() for result in game_data.split(';')]

        # Initialize a dictionary for the current game. Remove the word 'Game' to get just the ID
        # and convert it to an integer. Append the results to the dictionary. Append the dictionary
        # to the list. Repeat for each game in the file.

        game_dict = {'Game ID': int(game_number.strip("Game")), 'Results': []}

        # Process each result in the game and append to the dictionary
        for result in results:
            # Split each result based on commas to get colour and count
            colour_data = [item.strip().split() for item in result.split(',')]
            colours = {colour: int(count) for count, colour in colour_data}
            game_dict['Results'].append(colours)

        # Append the game dictionary to the list
        game_list.append(game_dict)

    return game_list


def convert_to_json(data):
    '''
    Extra function to convert the list of dictionaries and return JSON and write to a file
    Not required
    '''
    json_data = json.dumps(data)
    with open('output.json', 'w') as f:
        f.write(json_data)
        f.close()
        return json_data


def sum_of_possible_games(game_list):
    '''
    Which games would have been possible if the bag contained only
    12 red cubes, 13 green cubes, and 14 blue cubes?

    Example JSON
    {'Game ID': 1, 'Results': [{'green': 20, 'red': 3, 'blue': 2}, {'red': 9, 'blue': 16, 'green': 18}, {'blue': 6, 'red': 19, 'green': 10}, {'red': 12, 'green': 19, 'blue': 11}]}
    '''
    possible_games = []
    game_ids = []

    for game in game_list:
        max_count = 0
        for game_results in game['Results']:
            # Default value of 0 if green doesn't exist
            result_red = game_results.get('red', 0)
            result_green = game_results.get('green', 0)
            result_blue = game_results.get('blue', 0)
            if (result_red > RED_MAX) or (result_green > GREEN_MAX) or (result_blue > BLUE_MAX):
                max_count += 1
        if max_count == 0:
            possible_games.append(game)
            game_ids.append(game['Game ID'])

    return sum(game_ids)


def power_of_games(game_list):
    '''
    What is the minimum number of cubes required to play each game
    Return the power of RGB in a list

    Test JSON
    {'Game ID': 1, 'Results': [{'green': 20, 'red': 3, 'blue': 2}, {'red': 9, 'blue': 16, 'green': 18}, {'blue': 6, 'red': 19, 'green': 10}, {'red': 12, 'green': 19, 'blue': 11}]}
    Red = 19
    Green = 20
    Blue = 16
    Power = 19*20*16 = 6,080

    '''
    power_of_games = []

    for game in game_list:
        red_max = 0
        green_max = 0
        blue_max = 0
        for game_results in game['Results']:
            red_max = max(red_max, game_results.get('red', 0))
            green_max = max(green_max, game_results.get('green', 0))
            blue_max = max(blue_max, game_results.get('blue', 0))

        power_of_games.append(red_max*green_max*blue_max)

    return sum(power_of_games)


game_list = create_json(content)

print('Sum of possible games: ', sum_of_possible_games(
    game_list))  # Correct answer 2545

print('Sum of power of games: ', power_of_games(
    game_list))  # Correct answer 78111
