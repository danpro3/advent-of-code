# %% part 1

def find_neighbors(grid,r,c):
    n = 0
    for x,y in dirs:
        if grid[r+x][c+y] in '@x':
            n += 1
    return n

# main
# grid = open('inputs/input_04_test.txt','r').read().splitlines()
grid = open('inputs/input_04.txt','r').read().splitlines()
# print(grid)
# _ = [print(x) for x in grid]

# pad the grid
padstr = '.'*len(grid[0])
grid.insert(0,padstr)
grid.append(padstr)
for i in range(len(grid)):
    grid[i] = '.'+grid[i]+'.'
# _ = [print(x) for x in grid]

# search for accessable paper rolls
dirs = (-1,-1,),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
rows = len(grid)
cols = len(grid[0])
rolls = 0
for r in range(1,rows-1):
    for c in range(1,cols-1):
        if grid[r][c] == '@':
            if find_neighbors(grid,r,c) < 4:
                rolls += 1

# _ = [print(x) for x in grid]
print(f'accessible rolls = {rolls}')