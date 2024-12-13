# %% load input
# import re
# grid = 'AAAA\nBBCD\nBBCC\nEEEC'
# grid = grid.split('\n')
# grid = open('inputs/input_11_test.txt','r').read().splitlines()
grid = open('inputs/input_11.txt','r').read().splitlines()
# _=[print(x) for x in grid]
# print(grid)
rows = len(grid)
cols = len(grid[0])
# %% part 1

def move(todo):
    r,c,ID = todo.pop()
    G = grid[r][c]
    walls = 0
    dirs = [(-1,0), (0,-1), (1,0), (0,1)] # up, left, down, right
    for dir in dirs:
        dr, dc = dir
        if r+dr <  0 or r+dr == rows or c+dc < 0 or c+dc == cols:
            walls += 1  # edge wall
        if (r+dr >=0 and r+dr < rows and c+dc >= 0 and c+dc < cols and
        grid[r+dr][c+dc] != G):
            walls += 1 # inside wall
        if (r+dr >=0 and r+dr < rows and c+dc >= 0 and c+dc < cols and
        grid[r+dr][c+dc] == G): # inside same garden plot
            if (r+dr,c+dc) not in cache:
                todo.append((r+dr,c+dc,ID))
    if ID not in regions:
        regions[ID] = [(r, c, walls, G)]
    else:
        if (r,c) not in cache:
            regions[ID].append((r, c, walls, G))
    cache.add((r,c))
    return todo

ID = 0 # identify each unique region
regions = {}
cache = set()
for R in range(rows):
    for C in range(cols):
        # print(R,C)
        if (R,C) not in cache:
            todo = [(R,C,ID)]
            while todo:
                todo = move(todo)
            ID += 1
price = 0
for R in regions:
    # print(f'{R}, plot: {regions[R][0][3]}, area: {len(regions[R])}, perimeter: {sum([x[2] for x in regions[R]])}')
    price += len(regions[R])*sum([x[2] for x in regions[R]])

print(f'price = {price}')



# %%
print(cache)
len(cache)
print(grid)
print(regions)
[print(f' {R}  {regions[R]}') for R in regions]