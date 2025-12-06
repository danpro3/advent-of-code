# %% part 1
import re

# loop on the operations
def sum_the_columns(grid,ops):
    total = 0
    for c,op in enumerate(ops):
        if op == '+':
            quicktotal = 0
            for r in range(len(grid)):
                quicktotal += grid[r][c]
        else: # '*'
            quicktotal = 1
            for r in range(len(grid)):
                quicktotal *= grid[r][c]
        total += quicktotal
    return total

# lines = open('inputs/input_06_test.txt','r').read().splitlines()
lines = open('inputs/input_06.txt','r').read().splitlines()

# make a grid of numbers
grid = []
for line in lines[:-1]:
    intstrings = re.findall(r'\d+', line)
    # print(intstrings)
    grid.append([int(x) for x in intstrings])
# _=[print(x) for x in grid]

ops = re.findall(r'[*+]', lines[-1])
# print(ops)

total = sum_the_columns(grid,ops)
print(f'total = {total}')

# better method: transpose and do it
list2 = [x for x in zip(*grid)]
# print(list2)
# total it up
total = 0
for i,row in enumerate(list2):
    if ops[i] == '+':
        total += sum(row)
    else:
        total += math.prod(row)
print(f'total = {total}')


# %% part 2
import math

# lines = open('inputs/input_06_test.txt','r').read().splitlines()
lines = open('inputs/input_06.txt','r').read().splitlines()
ops = re.findall(r'[*+]', lines[-1])
# print(ops)

# make a grid then transpose it
grid = [list(line) for line in lines[:-1]]
# _ = [print(''.join(x)) for x in grid]
transposed_list = [list(row) for row in zip(*grid)]
# _ = [print(x) for x in transposed_list]

# join the lines, find the numbers
list2 = []
quicklist = []
for line in transposed_list:
    numstr = re.findall(r'\d+', ''.join(line))
    if not(numstr == []):
        quicklist.append(int(numstr[0]))
    else:
        list2.append(quicklist)
        quicklist = []
list2.append(quicklist)
# print(list2)
# print(ops)

# total it up
total = 0
for i,row in enumerate(list2):
    if ops[i] == '+':
        total += sum(row)
    else:
        total += math.prod(row)
print(f'total = {total}')
