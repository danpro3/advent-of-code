# %% load input
# import re
# grid = 'AAAA\nBBCD\nBBCC\nEEEC'
# grid = 'EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE'
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
for ID in regions:
    # print(f'{R}, plot: {regions[R][0][3]}, area: {len(regions[R])}, perimeter: {sum([x[2] for x in regions[R]])}')
    price += len(regions[ID])*sum([x[2] for x in regions[ID]])

print(f'price = {price}')



# %%

def get_sides(ID):
    # for each direction, if a cell needs a wall "above",
    # don't add it if the neighbor to the right needs it.  
    sides = 0
    # dirs = [(-1,0), (0,-1), (1,0), (0,1)] # up, left, down, right
    for info in regions[ID]:
        r,c,G = [info[i] for i in [0,1,3]]
        # check for wall above by looking at neighbor right
        if r-1 < 0 or (r-1 >= 0 and grid[r-1][c] != G): # needs a wall
            if c+1 == cols or (c+1 < cols and grid[r][c+1] != G) or ( # end of road
            (c+1 < cols and grid[r][c+1]) == G and (r-1 >= 0 and c+1 < cols and grid[r-1][c+1] == G)):  # region steps up
                sides += 1

        # check for wall right by looking at neighbor down
        if c+1 == cols or (c+1< cols and grid[r][c+1] != G): # needs a wall
            if r+1 == rows or (r+1 < rows and grid[r+1][c] != G) or ( # end of road 
            (r+1 < rows and grid[r+1][c]) == G and (r+1 < rows and c+1 < cols and grid[r+1][c+1] == G)):  # region steps up
                sides += 1

        # check for wall below by looking at neighbor left
        if r+1 == rows or (r+1 < rows and grid[r+1][c] != G): # needs a wall
            if c-1 < 0 or (c-1 >= 0 and grid[r][c-1] != G) or ( # end of road
            (c-1 >= 0 and grid[r][c-1]) == G and (r+1 < rows and c-1 >= 0 and grid[r+1][c-1] == G)):  # region steps up
                sides += 1

        # check for wall left by looking at neighbor up
        if c-1 < 0 or (c-1 >= 0 and grid[r][c-1] != G): # needs a wall
            if r-1 < 0 or (r-1 >= 0 and grid[r-1][c] != G) or ( # end of road
            (r-1 >= 0 and grid[r-1][c]) == G and (r-1 >= 0 and c-1 >= 0 and grid[r-1][c-1] == G)):  # region steps up
                sides += 1
        # print (r,c,sides)
    return sides
# _=[print(x) for x in grid]

# _=[print(f' {ID}  {regions[ID]}') for ID in regions]
total_price = 0
for ID in regions:
    sides = get_sides(ID)
    area = len(regions[ID])
    total_price += sides*area
    # print(f'ID: {ID}, {regions[ID][0][3]}, sides = {sides}, area = {area}')

print(f'total price = {total_price}')
