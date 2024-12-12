# %% load input
import re
grid = 'AAAA\nBBCD\nBBCC\nEEEC'
grid = grid.split('\n')
# grid = open('inputs/input_11_test.txt','r').read().splitlines()
# grid = open('inputs/input_11.txt','r').read().splitlines()
_=[print(x) for x in grid]
# print(grid)
rows = len(grid)
cols = len(grid[0])
# %%


NEED TO DEAL WITH UNIQUE REGIONS WITH SAME LETTER
NEED TO FIX WALLS
def check_region(r, c, G):
    dirs = [(-1,0), (0,-1), (-1,0), (0,1)] # up, left, down, right
    walls = 0
    for dir in dirs:
        dr, dc = dir
        if (r+dr >= 0 and r+dr < rows and c+dc >= 0 and c+dc < cols and
        grid[r+dr][c+dc] != G):
            walls += 1
    if (r-1 >= 0 and grid[r-1][c] == G) or (
        c-1 >= 0 and grid[r][c-1] == G):
        regions[G].append((r, c,walls))
    else:
        regions[G] = [(r, c, walls)]
    return 1

regions = {}
for r,line in enumerate(grid):
    for c,G in enumerate(line):
        # print(G, grid[r][c])
        a = check_region(r, c, G)

# print(regions)
[print(R, regions[R]) for R in regions]

