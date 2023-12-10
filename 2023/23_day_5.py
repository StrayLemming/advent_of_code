'''
23_day_5.py
https://adventofcode.com/2023
Day 5: If You Give A Seed A Fertilizer

Rubbish brute force attempt. Works for small dataset, but then totally fails for larger numbers.

'''

from dataclasses import dataclass


@dataclass
class SeedMap:
    seed: int = 0
    soil: int = 0
    fert: int = 0
    water: int = 0
    light: int = 0
    temp: int = 0
    hum: int = 0
    loc: int = 0


filename = './2023/puzzle_input_data/puzzle_input_day5.txt'
# filename = './2023/puzzle_input_data/puzzle_input_test_day5.txt'


seeds_str = "seeds:"
index = []
map_names = ["seed-soil", "soil-fert", "fert-water", "water-light",
             "light-temp", "temp-hum", "hum-loc"]


with open(filename, 'r') as file:
    lines = file.readlines()

# Get seeds and start_index for the data
for i, line in enumerate(lines):
    if seeds_str in line.strip():
        name, seeds = line.split(':')
        # Use set to remove duplicates
        seeds = set(int(x) for x in seeds.split())

    elif ":" in line.strip():
        index.append(i)

seeds = {seed: SeedMap() for seed in seeds}
# Create empty dict using the map names as keys
maps = {map: [] for map in map_names}

# Get the Map data and zip the source:dest number ranges
for i, name in enumerate(map_names):

    start_index = index[i] + 1

    for line in lines[start_index:]:
        if not line.strip():
            break
        else:
            # dest_start, source_start, length = map(int, line.split())
            dest_start, source_start, length = [int(x) for x in line.split()]

            source_nums = list(range(source_start, source_start+length))
            dest_nums = list(range(dest_start, dest_start+length))
            zipped = zip(source_nums, dest_nums)
            maps[name].extend(list(zipped))


for seed_num in seeds:
    seeds[seed_num].seed = seed_num

    for name in maps.keys():
        found = False

        for data in maps[name]:
            if data[0] == getattr(seeds[seed_num], name.split('-')[0]):
                setattr(seeds[seed_num], name.split('-')[1], data[1])
                found = True
                break

        if not found:
            setattr(seeds[seed_num], name.split('-')[1],
                    getattr(seeds[seed_num], name.split('-')[0]))


print(seeds.values())
