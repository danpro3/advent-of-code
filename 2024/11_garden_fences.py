# %% load input
import re
grid = open('inputs/input_11_test.txt','r').read().splitlines()
# grid = open('inputs/input_11.txt','r').read().splitlines()
_=[print(x) for x in grid]
print(grid)
# %%


def check_region():

    return 1




regions = {}
for r,line in enumerate(grid):
    for c,char in enumerate(line):
        print(char, grid[r][c])

        