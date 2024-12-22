# %% input
import functools
# filestr = open('inputs/input_19_test.txt','r').read().split('\n\n')
filestr = open('inputs/input_19.txt','r').read().split('\n\n')
towels = filestr[0].split(',')
designs = filestr[1].splitlines()
for i,towel in enumerate(towels):
    if towel[0] == ' ':
        towels[i] = towel[1:]
print(towels)
print(designs)

# %% part 1
# @functools.lru_cache
def check_design(design):
    if design in cache:
        return cache[design]
    num_ways = 0
    filtered_towels = [t for t in towels if design[0:len(t)] == t]
    # print(f'{design}, filtered_towels = {filtered_towels}')
    for towel in filtered_towels:
        if len(towel) == len(design):
            num_ways += 1
        else:
            newdesign = design[len(towel):]
            num_ways += check_design(newdesign)
    cache[design] = num_ways
    return num_ways

# main
cache = dict()
total_designs = 0
total_ways = 0
for i,design in enumerate(designs):
# for i,design in enumerate(['gbbr']):
    # print(f'design: {design} ...')
    num_ways = check_design(design)
    if num_ways > 0:
        total_designs += 1
        total_ways += num_ways
    print(f'design: {i+1} of {len(designs)}, {design}, total so far = {total_designs}, , total ways so far = {total_ways}')
print(f'total designs = {total_designs}, total ways = {total_ways}')
